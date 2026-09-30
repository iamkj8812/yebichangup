"""Render the session dashboard HTML from reports/dashboard-data.json.

Usage: python3 .claude/skills/session-report/scripts/build.py [--project-root PATH]
Writes reports/dashboard.html and a dated snapshot reports/history/<date>-<no>.html.
Standard library only.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = SKILL_DIR / "assets" / "template.html"
PLACEHOLDER = "__DASHBOARD_DATA__"
REQUIRED_KEYS = ("project", "stages", "differentiation", "open_questions", "next_actions", "sessions")


@dataclass
class BuildResult:
    dashboard_path: Path
    snapshot_path: Path


class DashboardDataError(ValueError):
    pass


def load_dashboard_data(data_path: Path) -> dict:
    dashboard_data = json.loads(data_path.read_text(encoding="utf-8"))
    missing_keys = [key for key in REQUIRED_KEYS if key not in dashboard_data]
    if missing_keys:
        raise DashboardDataError(f"dashboard-data.json에 필수 키가 없습니다: {', '.join(missing_keys)}")
    if not dashboard_data["sessions"]:
        raise DashboardDataError("sessions가 비어 있습니다. 이번 세션 항목을 추가하세요.")
    current_stages = [stage for stage in dashboard_data["stages"] if stage.get("status") == "current"]
    if len(current_stages) != 1:
        raise DashboardDataError(f"status가 'current'인 단계는 정확히 1개여야 합니다 (현재 {len(current_stages)}개).")
    return dashboard_data


def build_dashboard(project_root: Path) -> BuildResult:
    reports_dir = project_root / "reports"
    dashboard_data = load_dashboard_data(reports_dir / "dashboard-data.json")
    serialized_data = json.dumps(dashboard_data, ensure_ascii=False, indent=1).replace("</", "<\\/")
    rendered_html = TEMPLATE_PATH.read_text(encoding="utf-8").replace(PLACEHOLDER, serialized_data)

    dashboard_path = reports_dir / "dashboard.html"
    dashboard_path.write_text(rendered_html, encoding="utf-8")

    latest_session = dashboard_data["sessions"][-1]
    snapshot_dir = reports_dir / "history"
    snapshot_dir.mkdir(exist_ok=True)
    snapshot_path = snapshot_dir / f"{latest_session['date']}-{latest_session.get('no', 0):02d}.html"
    snapshot_path.write_text(rendered_html, encoding="utf-8")
    return BuildResult(dashboard_path=dashboard_path, snapshot_path=snapshot_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="세션 현황 보고서 HTML 생성")
    parser.add_argument("--project-root", type=Path, default=SKILL_DIR.parent.parent.parent)
    arguments = parser.parse_args()
    try:
        build_result = build_dashboard(arguments.project_root.resolve())
    except (DashboardDataError, json.JSONDecodeError, FileNotFoundError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"dashboard: {build_result.dashboard_path}")
    print(f"snapshot:  {build_result.snapshot_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
