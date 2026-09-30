# dashboard-data.json 형식

```json
{
  "project": {
    "title": "초등 코딩교육 관리 플랫폼 — 예비창업패키지 2027",
    "representative": "아내분",
    "deadline": "2027-02-20",
    "updated_at": "YYYY-MM-DD"
  },
  "stages": [
    {
      "id": 0, "name": "준비", "status": "done | current | todo",
      "done": 3, "total": 3, "target": "YYYY-MM-DD",
      "items": [ { "text": "통과 조건 문장", "done": false } ]
    }
  ],
  "differentiation": {
    "candidate": "후보 A — 한 줄 설명",
    "checks": [ { "name": "고객 문제와 연결", "status": "pass | partial | todo", "note": "짧은 근거" } ]
  },
  "open_questions": [ { "text": "질문", "stage": 1, "since": "YYYY-MM-DD" } ],
  "risks": [ { "text": "넘어간 항목과 위험", "stage": 2, "accepted_at": "YYYY-MM-DD" } ],
  "next_actions": [ "할 일" ],
  "sessions": [
    {
      "date": "YYYY-MM-DD", "no": 1, "title": "세션 한 줄 제목",
      "done": [ "한 일" ],
      "resolved": [ { "question": "풀린 고민", "answer": "답 / 근거 파일" } ],
      "decisions": [ "결정" ],
      "new_questions": [ "새 고민" ]
    }
  ]
}
```

## 규칙
- `stages`: 0~7단계 전부. `items`는 current 단계에만 넣으면 된다(다른 단계는 생략 가능). `done`/`total`은 roadmap.md 체크박스 개수.
- `status: "current"`는 정확히 1개 (build.py가 검사).
- `sessions`는 추가만 한다. 과거 세션을 고치지 않는다 — 기록이 흔들리면 히스토리의 의미가 없다.
- `no`는 전체 누적 세션 번호 (1, 2, 3 …).
- 문장은 대표님이 읽고 이해할 수 있는 쉬운 말로. 파일 경로는 `answer`의 근거 표시에만.
