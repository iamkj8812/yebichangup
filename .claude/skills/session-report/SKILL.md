---
name: session-report
description: 예비창업패키지 과제의 세션 현황 보고서를 대시보드형 그림 문서(Artifact)로 만든다. 지금 몇 단계인지, 통과 조건이 얼마나 채워졌는지, 이번 세션에서 해결된 고민·결정·새 고민, 남은 고민, 차별점 검증 상태, 다음 할 일을 한 화면에 보여준다. "오늘 여기까지", "세션 마무리", "정리하고 끝내자", "현황 보고서", "현황판", "대시보드 만들어줘", "지금 어디까지 왔어?", "진행 상황 보여줘", "보고서 업데이트"처럼 세션을 끝내거나 과제 진행 상황을 한눈에 보고 싶어 할 때 반드시 이 스킬을 쓴다. 사용자가 보고서를 명시적으로 부르지 않아도 세션 종료 신호가 보이면 쓴다.
---

# session-report — 세션 현황 보고서

세션을 끝낼 때마다 과제 상태를 **그림 문서(Artifact)** 로 남긴다. 텍스트 요약으로 대신하지 않는다. 사용자(남편분)와 대표님(아내분) 둘 다 이 한 장으로 "어디까지 왔고, 무엇이 남았고, 오늘 무엇이 풀렸는지"를 봐야 한다.

보고서는 과제 파일의 **거울**이다. 파일에 없는 진척을 보고서에 쓰면, 부족한 구상이 다음 단계로 넘어간 것처럼 보이게 된다(CLAUDE.md 4번 게이트 규칙이 막으려는 바로 그 악순환). 그래서 순서가 중요하다: **파일 먼저 최신화 → 그 파일에서 데이터 추출 → 렌더링**.

## 파일 위치 (과제 폴더 기준)
- 데이터: `reports/dashboard-data.json` — 누적 데이터. 세션마다 갱신·추가
- 결과: `reports/dashboard.html` (항상 최신) + `reports/history/<날짜>-<번호>.html` (스냅샷)
- Artifact URL: `reports/artifact-url.txt` — 같은 URL로 계속 갱신하기 위해 저장
- 템플릿·스크립트: 이 스킬의 `assets/template.html`, `scripts/build.py`
- 데이터 형식: `references/data-schema.md` (데이터를 고치기 전에 읽는다)

## 절차

### 1. 미기록분 먼저 기록
이번 세션 대화를 훑어서 아직 파일에 안 적힌 결정·고민·진행을 CLAUDE.md 6번 규칙대로 먼저 기록한다. `context/00-brief.md`도 갱신한다. 보고서는 이 파일들만 근거로 만든다.

### 2. 근거 파일 읽기
`context/roadmap.md`, `context/open-questions.md`, `context/decisions.md`, `context/differentiation.md`, `log.md`, 그리고 기존 `reports/dashboard-data.json`(없으면 새로 만든다).

### 3. 데이터 갱신 (`reports/dashboard-data.json`)
`references/data-schema.md`의 형식을 따른다. 핵심 규칙:
- **stages**: roadmap.md의 체크박스를 그대로 센다. `[x]`만 done. 현재 단계(`status: "current"`)는 정확히 하나이고, 그 단계의 `items`에 체크리스트 전체를 넣는다. 추측으로 체크하지 않는다.
- **differentiation.checks**: differentiation.md의 검증 현황을 옮긴다. ✅=pass, 🔶=partial, ⬜=todo.
- **open_questions**: open-questions.md의 `- [ ]` 항목 전부. 어느 단계 질문인지 `stage`, 처음 생긴 날짜 `since`(기존 데이터에 있으면 그대로 유지 — 고민이 며칠째인지 보여주는 값이다).
- **risks**: decisions.md에서 "리스크 수용"으로 기록된 항목.
- **next_actions**: 00-brief.md의 "다음 할 일"과 일치시킨다. 1~5개.
- **sessions**: 기존 항목은 건드리지 않고 이번 세션을 맨 뒤에 **추가**한다. 같은 날 여러 세션이면 `no`를 올린다.
  - `resolved`: 이번 세션에 open-questions에서 `[x]`로 바뀐 것과 그 답. 대화에서 풀렸지만 파일에 없던 것은 1단계에서 먼저 파일에 기록한 뒤 넣는다.
  - `decisions`: 이번 세션에 decisions.md에 추가된 줄
  - `new_questions`: 이번 세션에 새로 생긴 open question
  - `done`: 이번 세션에 한 일 3~6개. 대표님이 읽고 알아듣는 말로.
- `project.updated_at`을 오늘 날짜로.

### 4. 렌더링
```bash
python3 .claude/skills/session-report/scripts/build.py
```
스크립트가 필수 키, current 단계 개수를 검사한다. 에러가 나면 데이터를 고치고 다시 돌린다.
python3가 없으면: `assets/template.html`을 읽고 `__DASHBOARD_DATA__`를 JSON으로 바꿔(`</`는 `<\/`로) `reports/dashboard.html`에 직접 쓴다.

템플릿 디자인은 고정이다. 매번 새로 디자인하지 않는다 — 세션마다 같은 모양이어야 변화가 눈에 들어온다. 디자인을 바꾸고 싶다는 요청이 있을 때만 템플릿을 고친다.

### 5. 그림 문서로 게시
- Artifact 도구로 `reports/dashboard.html`을 게시한다.
- `reports/artifact-url.txt`에 URL이 있으면 그 URL을 `url`로 넘겨 **같은 주소를 갱신**한다(다른 대화에서 만든 문서라면 먼저 `read`로 읽고 게시). 없거나 권한이 없어 실패하면 새로 게시하고 URL을 파일에 저장한다.
- 첫 게시에는 `icon: "chart"`, description 한 문장.
- Artifact 도구가 없는 환경이면, `reports/dashboard.html`을 더블클릭해서 브라우저로 보라고 안내한다.

### 6. 마무리 보고
- `log.md` 오늘 날짜 아래에 "현황 보고서 갱신 (#번호)" 한 줄.
- 사용자에게: 링크, 그리고 3줄 요약 — **현재 단계와 통과 조건 진척 / 이번 세션에 풀린 것 / 다음에 할 일**. 현재 단계에서 막혀 있는 조건이 있으면 그것을 짚는다.

## 정직성 체크 (게시 전)
- 보고서의 done 개수가 roadmap.md 체크 개수와 같은가
- 이번 세션 "해결된 고민"이 open-questions.md에서 실제로 `[x]`인가
- 차별점 통과 개수가 differentiation.md와 같은가
하나라도 다르면 파일이 맞는지 데이터가 맞는지 확인하고 고친다. 보고서를 좋아 보이게 하려고 파일과 다른 값을 쓰지 않는다.
