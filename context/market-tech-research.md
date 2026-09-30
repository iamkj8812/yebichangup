# 초등 코딩/AI 교육 관리 플랫폼(LMS) — 시장·정책·기술 리서치

작성일: 2026-09-23
조사 방법: 웹 검색(WebSearch/WebFetch) 기반. 1차 출처(공식 문서·정부기관·GitHub LICENSE 원문)를 우선 확인했고, 확인 불가 항목은 "미확인"으로 표시. 추측 없음.

---

## 핵심 요약

1. **정책 순풍은 뚜렷함** — 2022 개정 교육과정으로 초등 정보교육 시수가 2배(17→34시간 이상)로 늘고, 2025년 초3~4·2026년 초5~6에 순차 적용 중. 늘봄학교(방과후) 전국 확대와 맞물려 코딩/AI 콘텐츠 수요가 구조적으로 커지는 국면.
2. **AI 디지털교과서(AIDT)는 역풍 국면** — 2025년 도입 후 활용률 저조(평균 8.1%)·구독료 급증 논란으로 법적 지위가 '교과서'에서 '교육자료'로 격하되어 의무 채택이 사라짐. 국가 주도 디지털교과서보다 민간 에듀테크 서비스가 학교 재량으로 채택될 여지가 커짐.
3. **저학년(1~2학년) 코딩교육의 교육과정상 명시적 확대 근거는 없음** — 2022 개정 교육과정에서 1~2학년은 국어 시수 확대가 핵심이고, 정보교육 34시간 확대는 5~6학년(실과) 대상. 저학년 코딩 수요는 늘봄학교·사교육 시장 쪽에서 나타나는 것으로, 교육과정 의무화 근거는 "미확인".
4. **시장 규모 수치는 출처별 편차가 크고 일부는 출처 불명확** — 국내 코딩교육 시장 "2019년 1500억→2030년 1조5000억"은 원 기사에 기관명 없이 "전문가들은"으로만 인용되어 신뢰도 낮음. 국내 에듀테크 전체 시장은 2025년 약 10조원(연평균 8.5% 성장) 추정이 상대적으로 근거가 명확함. 글로벌 K-12 코딩교육 시장은 2025년 38억 달러 → 2034년 116억 달러(CAGR 13.2%) 추정.
5. **블록코딩 엔진 선택이 사업 구조를 좌우함** — Scratch 웹 버전(scratch-gui/scratch-vm)은 2024년 말 AGPL-3.0으로 전환되어, 상업 서비스에 수정·임베드 시 수정 소스 공개 의무가 발생하는 강한 카피레프트 제약이 있음. 반면 Entry(entryjs)와 Google Blockly는 Apache 2.0으로 상업적 임베드·수정에 제약이 거의 없음. 저학년(5~7세) 대상 ScratchJr는 BSD-3-Clause이나 공식 웹 임베드용 라이브러리는 없고 네이티브 앱 배포 중심.
6. **경쟁사 지형** — 국내는 코드모스·엘리스스쿨처럼 공교육 연계형이 늘고 있고, 클래스팅·하이클래스는 코딩 전문이 아닌 범용 학급관리(LMS) 플랫폼. 해외는 Code.org(무료·비영리)·Tynker/CodeMonkey(유료 B2B, $25/학생 수준)가 표준적 가격대 형성.
7. **저학년 대상 규제는 개인정보(법정대리인 동의)·학교 조달(S2B)·CSAP 3축** — 만 14세 미만은 개인정보보호법 제22조의2에 따라 법정대리인 동의가 원칙. 공공(학교) 대상 클라우드 SaaS는 CSAP 인증이 사실상 진입장벽(비용 1900~2900만원, 소요 10개월~1년, 국내 SaaS 기업 중 CSAP 취득 후 공공 진출 비율 10% 미만)이며, 학교 개별 구매는 나라장터(G2B)가 아니라 교육기관 전용 S2B(학교장터)를 통하는 것이 일반적.

---

## 1. 정책/수요

### 1.1 2022 개정 교육과정 초등 정보교육 시수

- 초등학교 실과 교과 내 정보교육 단원 시수가 **17시간 → 34시간 이상**으로 2배 확대됨.
  - 출처: [전자신문 "내년 정보 수업 두 배로 늘어난다…교육부, 권고에서 의무로 변경"](https://www.etnews.com/20221109000132), [한국경제 "초등, 국어 늘리고…중학교, 정보교육 2배 확대"](https://www.hankyung.com/article/2022122247411)
- 적용 일정: 2024년 초1~2학년부터 개정 교육과정 시행 시작 → **2025년 초3~4학년, 중1, 고1로 확대** → **2026년 초5~6학년**까지 순차 적용. 즉 정보교육 34시간 확대가 실제 적용되는 학년은 5~6학년이며, 2026년(올해)에 전면 적용되는 시점.
  - 출처: [뉴시스 "'컴퓨터 언어' 코딩, 초등학교부터 배운다…2025년 적용"](https://www.newsis.com/view/NISX20220822_0001986131)
- 교육부는 2025년부터 정보수업 의무 시수를 **초등 34시간, 중학교 68시간 이상**으로 확대한다고 공식 발표(코딩교육을 정보 수업 내용에 포함해 의무화).
  - 출처: [더리포트 "2025년부터 초등학교에서 '컴퓨터 언어' 코딩 배운다"](https://www.thereport.co.kr/news/articleView.html?idxno=23172), [시민의소리 "2025년 부터 '코딩' 교육 초·중 의무적 시행"](https://www.siminsori.com/news/articleView.html?idxno=232220)
- 1~2학년은 이번 개정에서 **국어 시수가 448→482시간(34시간 확대)** 되는 것이 핵심 변화이며, 정보교육 확대는 명시되지 않음(1.4 참조).
  - 출처: [한국경제](https://www.hankyung.com/article/2022122247411)
- 참고(블로그, 2차 출처): [악어에듀 "2026 AI 교육 정책 총정리"](https://www.akeoedu.com/blog/ai-education-policy-2026-5-summary)

### 1.2 AI 디지털교과서(AIDT) 정책의 최신 상태 (2025~2026)

- **도입 현황(2025년)**: 초등학교 수학3·4, 영어3·4 / 중학교 수학1, 영어1, 정보 / 고등학교 공통수학1·2, 공통영어1·2, 정보 / 초등 특수학교 국어3·4 과목에 도입.
  - 출처: [교육부 공지](https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=294&boardSeq=101774&lev=0&searchType=null&statusYN=W&page=1&s=moe&m=020402&opType=N)
- **활용률 저조**: 2025년 AIDT 자율 선정 학교 점검 결과, 단 1회도 접속하지 않은 학생 비율 평균 **60%**, 평균 활용률 **8.1%**.
  - 출처: [edumorning "[2026 교육부 정책분석①] AI 디지털교과서 이후"](https://edumorning.com/articles/1558)
- **구독료 급증 우려**: 감사원 추계 기준 AIDT 구독료가 **2025년 3,361억원 → 2026년 5,421억원 → 2027년 8,634억원 → 2028년 1조732억원**으로 급증 전망.
  - 출처: [한국데이터경제신문 "[단독분석] 1조 4천억 AI 교과서, 483만 학생의 데이터는 누구의 것인가"](https://www.dataeconomy.co.kr/news/articleView.html?idxno=35458)
- **법적 지위 변경(핵심 변화)**: AIDT의 법적 지위가 **'교과서'에서 '교육자료'로 격하**되어 의무 채택이 사라지고 학교 자율 선택제로 전환됨.
  - 출처: [교육을 비추다 "'교과서' 떼고 '자료' 된 AIDT... 2026년 확대 정책 '유명무실' 우려"](https://www.kyobit.com/news/articleView.html?idxno=3879), [교풀 "AI 디지털교과서 폐지인가요? 2026년 달라진 점 총정리"](https://www.gyopool.com/blog/ai-digital-textbook-overview-2026)
- **2026년 도입 일정 조정 논의**: 2026년 도입 예정이던 국어·기술가정 AIDT의 시행 시기 연기가 검토 중이며, 교육부-시도교육감협의회 간 협의 진행 중.
  - 출처: [에듀프레스 "[단독] AI디지털교과서, 2026년 국어, 기술·가정 제외 논의"](https://www.edupress.kr/news/articleView.html?idxno=12359)

**창업 아이템 시사점**: AIDT가 '교과서'에서 '교육자료'로 격하되며 국가 주도 디지털교과서의 학교 현장 침투력이 약화됨. 이는 민간 에듀테크가 개별 학교/교사 재량으로 채택될 여지가 커진다는 의미이나, 동시에 학교의 '피로도'(AIDT 저활용 논란)가 신규 디지털 도구 도입에 대한 경계심을 키울 가능성도 있음.

### 1.3 늘봄학교(방과후) 코딩/AI 수요

- 늘봄학교는 초등학생을 오후 8시까지 학교에서 돌봄+방과후 형태로 운영하는 정책으로, **2025년 전국 확대**가 진행됨.
  - 출처: [이데일리 "'돌봄교실 8시까지 운영'…초등늘봄학교 2025년 전국 확대"](https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=02774886635476080)
- 늘봄학교 프로그램에서 AI·코딩·빅데이터·드론 교육 등이 다양화되는 추세이며, 학생/학부모 수요를 반영해 프로그램 구성 중.
  - 출처: [아시아경제 "미래 설계하는 아이들… 부산교육청, AI·코딩 교육 확대"](https://view.asiae.co.kr/article/2026062210274041362), [네이트뉴스 "부산교육청, 늘봄전용학교 AI 교육으로 디지털 소양 강화"](https://m.news.nate.com/view/20260109n21303)
- 지역 사례: 충남 상명대가 '충남 라이즈 늘봄학교' 관련 AI코딩·디자인·문화예술 콘텐츠 참여, 소규모 학교 대상 '찾아가는 늘봄학교 AI 활용 프로그램' 운영(지역 디지털교육 격차 해소 목적).
  - 출처: [서울Pn "상명대, 'AI코딩 등' 방과 후 교육콘텐츠 호응"](https://go.seoul.co.kr/news/newsView.php?id=20250727500093)
- 교육부는 관련 돌봄·교육 프로그램 개발을 위해 전국 **230개교**를 선정(2026년).
  - 출처: 늘봄허브(한국과학창의재단) 관련 검색 결과 종합, [늘봄허브](https://neulbomhub.kosac.re.kr/hmpg/main/main.do)
- **외부 에듀테크 업체의 늘봄학교 참여 구조(강사 매칭/콘텐츠 공급 계약 형태, 정산 방식 등 세부)**: 미확인 — 일반 뉴스에서 참여 사례는 확인되나 계약/공급 구조에 대한 공식 가이드라인 문서는 이번 조사에서 찾지 못함.

### 1.4 초등 저학년(1~2학년) 코딩교육 확대 여부

- **교육과정상 근거**: 2022 개정 교육과정에서 1~2학년의 핵심 변화는 **국어 시수 확대(448→482시간)**이며, 정보교육(코딩) 시수 확대는 **5~6학년 실과** 과목에 한정됨. 1~2학년에 정보교육이 정규 교과로 명시적으로 확대된다는 근거는 **미확인**(오히려 국어 강화가 우선순위였다는 것이 확인된 사실).
  - 출처: [한국경제](https://www.hankyung.com/article/2022122247411)
- **저학년 코딩 수요의 근거**: 정규 교육과정이 아닌 **늘봄학교·사교육 시장**에서 저학년 대상 코딩 프로그램이 존재함을 뉴스 사례로 확인(1.3 참조). 다만 이것이 "확대"라고 할 만한 정량적 통계(저학년 코딩 학원 수강생 증가율 등)는 이번 조사에서 **미확인**.
- 시장 측 근거로는 코드모스가 "유아, 초등 저학년부터 중학교 3학년까지" 커버한다고 밝히고 있어, 민간 서비스 차원에서는 저학년 시장을 이미 타겟팅하고 있음이 확인됨.
  - 출처: [코드모스 서비스 소개](https://blog.codmos.io/codmos-%EC%84%9C%EB%B9%84%EC%8A%A4-%EC%86%8C%EA%B0%9C%EC%84%9C)

---

## 2. 시장 규모

### 2.1 국내 코딩교육/에듀테크 시장

| 항목 | 수치 | 출처/신뢰도 |
|---|---|---|
| 국내 초중고 코딩교육 시장 | 2019년 1,500억원 → 2030년 1조5,000억원(전망) | [더스탁](https://www.the-stock.kr/news/articleView.html?idxno=20099) — **주의: 기사 내 "전문가들은"으로만 인용, 구체적 발표 기관명 없음. 신뢰도 낮음.** |
| 코딩 부트캠프 시장(글로벌 인포메이션(GII) 발표) | 2022~2027 연평균 19.77% 성장, 2027년 약 14억 8,487만 달러(≈2조500억원) 규모 전망 | [더스탁](https://www.the-stock.kr/news/articleView.html?idxno=20099) — K-12 특화 수치는 아니고 코딩 부트캠프(성인 포함) 전체 시장 |
| 국내 에듀테크 시장 | 2021년 약 7조3,250억원 → 연평균 8.5% 성장 → 2025년 약 9조9,833억원(약 10조원) 전망 | [한경매거진&북 / KT Enterprise 등 종합](https://enterprise.kt.com/bt/dxstory/754.do) — 상대적으로 근거 명확, 단 K-12 코딩교육만의 세부 breakdown은 아님 |
| 글로벌 에듀테크 시장(HolonIQ) | 2025년 4,040억 달러(약 532조원) 전망 | [사이다경제](https://cidermics.com/contents/detail/2118) |

- 추가로 KOTRA/무역협회(KITA) 자료 [에듀테크(Edutech) 시장 현황 및 시사점](https://kita.net/board/pressData/fileDownload.do?no=3A4C039BECE7D28523D598B95B309D24&seq=2), 네이버 pstatic 게재 [2025년 한국 에듀테크 산업 및 디지털 교육혁신 시장 종합 분석 보고서](https://files-scs.pstatic.net/2025/02/27/4mWAAoFOE8/2025%EB%85%84%20%EC%97%90%EB%93%80%ED%85%8C%ED%81%AC%EC%82%B0%EC%97%85%20%EB%B0%8F%20%EB%94%94%EC%A7%80%ED%84%B8%20%EA%B5%90%EC%9C%A1%ED%98%81%EC%8B%A0%20%EC%8B%9C%EC%9E%A5%20%EC%A2%85%ED%95%A9%20%EB%B6%84%EC%84%9D%20%EB%B3%B4%EA%B3%A0%EC%84%9C(1%EC%B0%A8).pdf%29)가 검색되었으나, 본 조사에서는 원문 PDF까지 열람해 수치를 대조하지 못함 — 정밀 인용이 필요하면 추가 확인 필요(미확인).
- **국내 K-12 코딩교육 전용 시장 규모를 발표한 공신력 있는 기관(NIPA, 한국에듀테크산업협회, 통계청 등) 공식 수치**: 이번 조사에서는 찾지 못함 — **미확인**.

### 2.2 해외 K-12 coding education 시장

| 항목 | 수치 | 출처 |
|---|---|---|
| K12 Coding Courses Market | 2025년 38억 달러 → 2034년 116억 달러, CAGR 13.2% | [Dataintelo](https://dataintelo.com/report/global-k12-coding-courses-market) |
| Coding Education Market(전체, K-12 한정 아님) | 2024년 147억 달러 → 2033년 614억 달러, CAGR 18.2%(2025~2033) | [Growth Market Reports](https://growthmarketreports.com/report/coding-education-market) |
| K-12 Education Market(코딩 한정 아닌 전체 K-12 교육 시장) | 2034년까지 732.94억 달러, CAGR 17.47% | [GlobeNewswire / Custom Market Insights](https://www.globenewswire.com/news-release/2025/04/29/3069912/0/en/Latest-Global-K12-Education-Market-Size-Share-Worth-USD-732-94-Billion-by-2034-at-a-17-47-CAGR-Custom-Market-Insights-Analysis-Outlook-Leaders-Report-Trends-Forecast-Segmentation-G.html) |
| Grand View Research K-12 Education Market Report | 별도 수치 존재(원문 미열람) | [Grand View Research](https://www.grandviewresearch.com/industry-analysis/k-12-education-market-report) — **미확인**(리포트 링크만 확인, 본문 수치 미열람) |

- 여러 시장조사기관이 유사한 방향성(연 13~18% 성장)을 제시하나, 조사기관별 정의(코딩교육 vs K-12 교육 전체 vs edtech 전체)가 달라 수치 편차가 큼. 특정 수치를 인용할 때는 반드시 "어느 세그먼트를 정의한 수치인지" 원문 대조가 필요함.

---

## 3. 경쟁사 비교

| 서비스명 | 국가 | 대상 연령 | 교사용 관리(LMS) 기능 | 가격 | 차별점 | 출처 |
|---|---|---|---|---|---|---|
| **엘리스스쿨(elice school)** | 한국 | 초·중·고 (학교 단위 계약) | 있음 — "학교를 위한 안전한 AI 수업 플랫폼" 표방 | 1개 학사년도 계약 기준 학생 계정 1개당 1만원 + 과목별 콘텐츠 이용료(상세 미확인) | 공교육(정보 교과) 채택 중심, AI 시대 실습 플랫폼 지향 | [엘리스스쿨](https://school.elice.io/), [AskEdTech 제품정보](https://www.askedtech.com/product-information/product-detail/674cc374797227dada9ba367) |
| **코드모스(CODMOS)** | 한국 | 유아~초등 저학년~중3 | 코드모스 스쿨(교육기관용) 별도 존재, 세부 기능 상세는 미확인 | 미확인 | SW/AI 공교육 채택률 1위 자칭, 누적 학습자 250만 명 데이터 기반, 2022 개정 교육과정 + 미국 CSTA 기준 반영 | [코드모스 소개](https://blog.codmos.io/codmos-%EC%84%9C%EB%B9%84%EC%8A%A4-%EC%86%8C%EA%B0%9C%EC%84%9C), [코드모스 스쿨](https://school.codmos.io/plan) |
| **코딩앤플레이** | 한국 | 미확인(프랜차이즈 학원 형태로 추정) | 미확인 | 미확인(프랜차이즈 가맹 비용 별도) | 코딩교육 전문 프랜차이즈 — 온라인 LMS라기보다 오프라인 학원 체인 성격으로 추정(확인 필요) | [코딩앤플레이](http://codingnplay.co.kr/en/emain/) |
| **알공(Argong)** | 한국 | 초3~6 | LMS 있음("알공3 LMS") | 미확인 | ⚠️조사 결과 코딩교육이 아니라 **영어·수학 AI 코스웨어**로 확인됨(과기정통부 디지털서비스 등록). 사용자가 예시로 든 것과 달리 코딩 경쟁사가 아닐 가능성 높음 — 재확인 필요 | [알공 공식](https://www.argong.ai/), [알공3 LMS](https://manager.argong.ai/) |
| **클래스팅** | 한국 | 초·중·고 전반(코딩 전문 아님, 범용 LMS) | 있음 — 학급 공지, 과제, 1:1 톡, AI 학습 경로 추천 | 소프트웨어 사용료 1인 1개월 2만원(VAT별도) 기준, 학교별 견적 상이 | SNS+LMS 결합, AI 기반 개인화 학습, 범용 학급관리 플랫폼(코딩 특화 아님) | [클래스팅 요금제](https://www.classting.com/pricing), [도입비용 안내](https://support.classting.com/hc/ko/articles/19328333734425-%EB%8F%84%EC%9E%85-%EB%B9%84%EC%9A%A9%EC%9D%B4-%EC%96%BC%EB%A7%88%EC%9D%B8%EA%B0%80%EC%9A%94) |
| **하이클래스** | 한국 | 초등 전용 | 있음 — 출결관리, 누가기록, 알림장, 앨범, 스마트 칠판 연동 | 학교에 별도 비용 없이 제공(구체 수익모델 미확인, i-Scream 계열사 추정) | 전국 5,000여개 초등학교 사용 중, 코딩 전문이 아닌 학급 운영 올인원 플랫폼 | [하이클래스](https://www.hiclass.net/), [i-Screammedia 소개](https://www.i-screammedia.com/www/business_hiclass.html) |
| **Code.org** | 미국(비영리) | K-12 전체 | 있음(무료 교사 대시보드, Hour of Code 커리큘럼) | 무료(비영리 재단 운영) | 전 세계 최대 규모 무상 CS교육 커리큘럼, Google/MS 등 후원 | [Code.org vs Tynker (Tynker Blog)](https://www.tynker.com/blog/code-org-vs-tynker/) |
| **Tynker** | 미국 | K-12(주로 초·중) | 있음 — 진도 대시보드(교사/학부모) | 학교 플랜 학생당 $25(최소 100명), 개인 자율학습 월 $20~, 1:1 코스 $199 | 1,600시간 이상 K-12 커리큘럼, Code.org 대비 심화·포괄적 | [Tynker 요금 비교](https://www.myengineeringbuddy.com/blog/tynker-reviews-alternatives-pricing-offerings/), [Code.org vs Tynker](https://www.tynker.com/blog/code-org-vs-tynker/) |
| **CodeMonkey** | 이스라엘/미국 | 저학년~중학생 중심 | 있음 — 수업계획, 채점, 진도추적, 클래스룸 대시보드 | 학교 플랜 학생당 $25(최소 100명), 가정용 연 $240(5학생+교사 2계정 포함) | 어린 연령대(코딩 입문) 특화, 게임 기반 학습 | [SaaSHub 비교](https://www.saashub.com/compare-codemonkey-vs-tynker), [Tynker vs CodeMonkey](https://edtechimpact.com/compare/tynker-vs-codemonkey/) |
| **ScratchJr(앱)** | 미국(MIT/Scratch Foundation) | 5~7세(유아~초1) | 없음(가정/개별 학습용 앱, 교사 관리 기능 없음) | 무료 앱 | 텍스트 없는 터치 기반 코딩, 가장 어린 연령대 타겟 | [ScratchJr GitHub](https://github.com/LLK/scratchjr) |
| **Google Classroom(코딩 연동 관점)** | 미국(Google) | 전연령 | 있음(범용 LMS, Classroom API 제공) | 무료(교육용 Google Workspace) | 코딩 전문 플랫폼이 아니라 범용 LMS — Code.org 등 외부 코딩 서비스와 연동해 쓰는 인프라 역할. Code.org와의 공식 직접 연동 세부 사항은 **미확인** | [Google Classroom API](https://developers.google.com/workspace/classroom) |

**관찰**: 국내 클래스팅·하이클래스는 코딩 전문이 아닌 범용 학급관리 LMS이고, 코딩 전문(코드모스·엘리스스쿨)은 상대적으로 교사용 관리 기능의 완성도·가격 정보가 외부에 잘 공개되어 있지 않음. 이는 "코딩 학습 콘텐츠 + 교사/학급 관리(LMS)"를 동시에 강하게 결합한 국내 사업자가 상대적으로 드물다는 시사점 — 사용자의 사업 아이디어(교사·학생·관리자용 통합 LMS)가 이 틈새를 겨냥할 여지가 있어 보이나, 이는 조사자의 해석이며 별도의 정성 검증(교사 인터뷰 등)이 필요함.

---

## 4. 블록코딩 도구 라이선스·기술 비교

### 4.1 Scratch (scratch-gui / scratch-vm)

- **라이선스**: 공식 레포([scratchfoundation/scratch-gui](https://github.com/scratchfoundation/scratch-gui/blob/develop/LICENSE), [scratchfoundation/scratch-vm](https://github.com/scratchfoundation/scratch-vm/blob/develop/LICENSE)) 모두 **GNU Affero General Public License v3 (AGPL-3.0)**. 원문 첫 줄로 직접 확인.
- **전환 배경**: 원래 BSD-3-Clause였으나, 상업 업체들이 Scratch 에디터를 가져다 클로즈드소스로 수익화하면서 프로젝트에 기여하지 않는 사례가 늘자 AGPL로 전환. Scratch Foundation은 기여자 라이선스 계약(CLA)을 통해 재라이선싱 권한을 보유.
  - 출처: [Discuss Scratch "Scratch is now AGPL"](https://scratch.mit.edu/discuss/post/8288467/), [ScratchAddons GitHub Discussion #7958](https://github.com/ScratchAddons/ScratchAddons/discussions/7958)
- **상업 임베드 시 제약**: AGPL은 네트워크 서비스(SaaS)로 제공되는 경우에도 카피레프트 의무가 적용되는 강한 라이선스. **scratch-gui/scratch-vm을 수정해서 자사 서비스에 네트워크로 제공하면, 수정한 소스 코드를 이용자에게 공개해야 할 의무**가 발생함. 수정 없이 원본 그대로 쓰는 경우는 원본 소스가 이미 공개돼 있어 실무상 문제가 적지만, 브랜딩/UI/기능을 커스터마이징하려는 상업 서비스 입장에서는 **자사 커스터마이징 코드 공개 의무**가 핵심 리스크.
- **상표(Trademark) 제약**: Scratch 이름·로고·Scratch Cat·Gobo/Pico/Nano/Tera/Giga 캐릭터는 Scratch Foundation 소유 상표. **명시적 라이선스 없이 이 상표를 제품/서비스 홍보·라벨링에 상업적으로 사용하는 것은 금지**. Scratch 웹사이트·언어 자체를 "지칭"하는 용도로만 제한적 사용 가능.
  - 출처: [scratch-gui/TRADEMARK](https://github.com/scratchfoundation/scratch-gui/blob/develop/TRADEMARK), [scratch-www/TRADEMARK](https://github.com/LLK/scratch-www/blob/develop/TRADEMARK)
- **.sb3 파일 포맷**: ZIP 아카이브 안에 `project.json`(블록·스프라이트·변수 등 프로젝트 데이터)과 미디어 파일(costume/sound, MD5 해시 파일명)로 구성. 포맷 자체는 공개되어 있고 파서 문서도 커뮤니티 위키에 존재.
  - 출처: [Scratch Wiki: Scratch File Format](https://en.scratch-wiki.info/wiki/Scratch_File_Format)

### 4.2 ScratchJr

- 공식 레포: [LLK/scratchjr](https://github.com/LLK/scratchjr) — **LICENSE 원문 확인 결과 BSD-3-Clause 계열**(상업적 사용 제한 없음, 저작권 고지 유지 의무만 있음).
- **형태**: 5~7세(유아~초1) 대상 **네이티브 앱**(iOS/Android/Chromebook/Windows/Mac)으로 배포되며, Scratch 3(웹)처럼 웹 임베드를 위한 공식 라이브러리·SDK는 확인되지 않음. 커뮤니티가 만든 비공식 웹/데스크톱 포트(scratchjr-desktop, ScratchJr-web 등)는 존재하나 **공식 지원 아님**.
- **상업적 임베드 가능 여부**: 라이선스(BSD)만 보면 상업적 재사용에 법적 제약은 적으나, 공식적으로 "임베드 가능한 웹 컴포넌트" 형태로 제공되지 않는다는 점이 실무적 제약. 자체 개발/포크가 필요.

### 4.3 Entry (엔트리, entryjs)

- **운영 주체**: 네이버 커넥트재단(비영리) 산하 엔트리(엔트리랩스). 공식 GitHub: [entrylabs/entryjs](https://github.com/entrylabs/entryjs) — "HTML5 기반 블록코딩 라이브러리"로 소개됨.
- **라이선스**: 검색 및 원문 대조 결과 **Apache License 2.0**. 상업적 이용·수정·배포 모두 허용, 저작권 고지 및 변경사항 명시 의무만 있음(무보증).
- **외부 서비스 임베드**: 공식 문서([Entry Docs: EntryJS 실행하기](https://docs.playentry.org/entryjs/started/2024-03-05-run.html))에서 자사 웹페이지에 entryjs를 로드해 실행하는 방법을 공식적으로 안내 — **엔진(에디터) 자체의 임베드는 공식 지원**. 단, playentry.org 사이트의 계정 시스템·학급(클래스) 기능·작품 공유 소셜 기능은 entryjs 라이브러리와 별개로 playentry.org 자체 서비스이며, **이 기능들을 제3자 서비스가 API로 끌어다 쓸 수 있는 공식 연동 API/SDK는 확인되지 않음**(미확인). 즉 "에디터 엔진"은 임베드 가능하지만 "엔트리의 학급 관리 기능"은 재사용이 아니라 자체 구축이 필요.
- **엔트리 자체의 학급(교사) 관리 기능**: playentry.org 내 "나의 학급" 기능으로 교사가 학급 개설, 학생 계정(ID/비번) 생성·엑셀 다운로드, 임시 비밀번호 발급, 학생 작품 확인 등 지원.
  - 출처: [playentry.org 나의 학급](https://playentry.org/group), [엔트리 학급 기능 메뉴얼(PDF)](https://playentry.org/uploads/%EC%97%94%ED%8A%B8%EB%A6%AC%20%ED%95%99%EA%B8%89%20%EA%B8%B0%EB%8A%A5%20%EB%A9%94%EB%89%B4%EC%96%BC.pdf)
- **한국 교과서 채택 현황**: playentry.org에 "미래엔 초등 실과", "비상교육 초등 실과" 등 출판사별 실과 교과서 연계 페이지가 존재해, **엔트리가 초등 실과 검인정 교과서 학습과 연계되어 활용되고 있음은 확인**됨. 다만 "엔트리가 교과서 자체에 공식 채택 교구로 지정되었는지"에 대한 교육부/교과서 검인정 공식 문서 차원의 확증은 **미확인**(출판사 연계 페이지 존재만 확인).
  - 출처: [playentry.org 미래엔 초등 실과](https://playentry.org/miraenCoding), [playentry.org 비상교육 초등 실과](https://playentry.org/visangEmt)

### 4.4 Google Blockly

- 공식 레포(2024년 Google → **Raspberry Pi Foundation으로 이관**): [google/blockly](https://github.com/google/blockly) (현재는 RaspberryPiFoundation 조직에서 관리) — **Apache License 2.0** 확인.
- **성격**: Blockly는 완성된 학습 서비스가 아니라 **블록 코딩 에디터를 만들기 위한 프레임워크/라이브러리**. 스프라이트, 스테이지, 게임 실행기 같은 "완성형 학습 경험"은 자체 구축해야 함(Scratch/Entry 대비 초기 개발 공수 큼).
- **상업적 이용 제약**: Apache 2.0으로 상업적 이용·수정·재배포 모두 자유로움. Google/Raspberry Pi Foundation 브랜드 사용 제약은 프레임워크 자체와는 무관(자체 제품명으로 자유롭게 출시 가능).
  - 출처: [Wikipedia: Blockly](https://en.wikipedia.org/wiki/Blockly), [blockly-android LICENSE](https://github.com/google/blockly-android)

### 4.5 비교 요약표

| 도구 | 라이선스(원문 확인) | 상업적 임베드 | 상표/브랜드 제약 | 주요 제약·특이사항 |
|---|---|---|---|---|
| **Scratch (scratch-gui/vm)** | AGPL-3.0 | 가능하나 **수정 시 소스 공개 의무**(강한 카피레프트) | Scratch 이름·로고·캐릭터 상업적 사용 금지(라이선스 필요) | 상업 SaaS에 커스터마이징해 임베드하기엔 리스크 큼 |
| **ScratchJr** | BSD-3-Clause | 라이선스상 자유로우나 **공식 웹 임베드 라이브러리 없음**(네이티브 앱 중심) | 미확인(별도 상표 정책 미확인) | 5~7세 특화, 웹 서비스 통합에는 자체 개발 필요 |
| **Entry (entryjs)** | Apache 2.0 | **에디터 엔진 임베드 공식 지원** | 엔트리/커넥트재단 브랜드 사용 제약 미확인(단, "엔트리"라는 명칭·로고 자체 사용은 별도 확인 필요) | 학급관리 등 부가 기능은 자체 구축 필요, 한국 교육과정 친화적 |
| **Google Blockly** | Apache 2.0 | 완전 자유 | 없음(프레임워크이므로 브랜드 이슈 자체가 거의 없음) | 완성 서비스가 아닌 프레임워크 — 개발 공수 가장 큼 |

**창업 아이템 시사점(사실 기반 요약, 조사자 해석 포함)**: 법적 리스크 최소화 관점에서는 **Entry(Apache 2.0) 또는 Blockly(Apache 2.0)**가 Scratch(AGPL)보다 상업 서비스에 안전하게 통합 가능함이 라이선스 원문으로 확인됨. 다만 Entry는 "완성형 에디터+한국 교육과정 친화성"을 제공하는 대신 학급관리 등 부가기능 재사용 범위가 불명확하고, Blockly는 완전한 자유도를 주는 대신 게임/스테이지 엔진을 처음부터 만들어야 함. Scratch를 쓰고 싶다면 "수정 없이 그대로 사용"하는 방식으로 AGPL 리스크를 최소화하는 선택지도 있으나, 이 경우 자체 브랜딩·UI 커스터마이징의 폭이 제한됨.

---

## 5. 저학년 대상 규제/고려사항

### 5.1 만 14세 미만 개인정보 처리

- **법적 근거**: 개인정보 보호법 **제22조의2 (아동의 개인정보 보호)** 제1항 — 개인정보처리자는 만 14세 미만 아동의 개인정보를 처리하기 위해 이 법에 따른 동의를 받아야 할 때는 **법정대리인의 동의**를 받아야 하며, 법정대리인이 동의했는지 확인해야 함.
  - 출처: [국가법령정보센터 조문](https://www.law.go.kr/LSW//lsLinkCommonInfo.do?lsJoLnkSeq=1029334873&chrClsCd=010202&ancYnChk=), [CaseNote 개인정보 보호법 제22조의2](https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4_%EB%B3%B4%ED%98%B8%EB%B2%95/%EC%A0%9C22%EC%A1%B0%EC%9D%982)
- **예외**: 법정대리인 동의를 받기 위해 필요한 최소한의 정보(대통령령으로 정함)는 법정대리인 동의 없이 아동으로부터 직접 수집 가능.
- **아동 자기결정권 존중**: 개인정보보호위원회는 만 14세 미만 아동도 개인정보 자기결정권의 주체이므로, 법정대리인에게만 동의를 구하고 아동의 자유의사를 무시해서는 안 된다는 기준을 제시한 바 있음.
  - 출처: [privacy.go.kr 법정대리인의 역할](https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=75), [nepla.ai 위키](https://www.nepla.ai/wiki/it-%EC%A0%95%EB%B3%B4-%EB%B0%A9%EC%86%A1%ED%86%B5%EC%8B%A0/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4-%EC%9C%84%EC%B9%98%EC%A0%95%EB%B3%B4-%EC%8B%A0%EC%9A%A9%EC%A0%95%EB%B3%B4/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4%EC%9D%98-%EC%B2%98%EB%A6%AC%EC%97%90-%EB%8C%80%ED%95%9C-%EC%A0%81%EB%B2%95%ED%95%9C-%EB%8F%99%EC%9D%98%EB%A5%BC-%EB%B0%9B%EB%8A%94-%EB%B0%A9%EB%B2%95/%EB%A7%8C-14%EC%84%B8-%EB%AF%B8%EB%A7%8C-%EC%95%84%EB%8F%99%EC%9D%98-%EB%B2%95%EC%A0%95%EB%8C%80%EB%A6%AC%EC%9D%B8-%EB%8F%99%EC%9D%98-%EC%A0%88%EC%B0%A8-rv5n71yqnzm4)
- **학교→에듀테크 업체 개인정보 위탁 절차의 세부 표준 계약서/가이드라인**: 이번 조사에서 교육부/개인정보보호위원회의 학교-에듀테크 위탁 전용 표준 가이드라인 존재 여부는 **미확인**(일반 개인정보 위탁 규정만 확인). 별도 확인 필요.

### 5.2 CSAP (클라우드서비스 보안인증)

- **근거 법령**: 「클라우드컴퓨팅 발전 및 이용자 보호에 관한 법률」 제23조의2.
  - 출처: [isms.kisa.or.kr CSAP 소개](https://isms.kisa.or.kr/main/csap/intro/)
- **인증 유형**: IaaS, SaaS, DaaS. **등급**: 상/중/하 3단계. **유효기간**: 5년(최초평가 → 매년 사후평가 → 5년마다 갱신평가).
- **교육기관 대상 SaaS의 CSAP 필수 여부**: 공공(학교 포함) 부문에 클라우드 SaaS를 제공하려면 **CSAP 인증이 사실상 필수 관문**(정부·공공기관 클라우드 이용 시 CSAP 인증 서비스만 이용 가능하도록 규정된 것이 일반적 실무 — 단, "학교 대상 서비스 전체"에 예외 없이 적용되는지의 세부는 이번 조사에서 100% 확증하지 못함, 대체로 필수로 통용됨).
  - 출처: [SK쉴더스 "국가·공공기관 클라우드 보안 서비스 공급 필수관문, 'CSAP' 란?"](https://www.skshieldus.com/blog-security/security-trend-idx-15)
- **소요 기간/비용**: 평가 자체는 2~3주지만, 서류 준비 포함 전체 소요는 **10개월~1년**. 비용은 중소기업 지원 반영해도 **1,900만~2,900만원** 수준(정부 개선안으로 중소기업 수수료를 평균 1,100만원→500만원으로 낮추는 방안이 추진 중).
  - 출처: [디지털투데이 "CSAP 인증 받기 만만 찮네...관련 업계 '비용 부담'"](https://www.digitaltoday.co.kr/news/articleView.html?idxno=508942), [뉴시스 "심사기간 평균 5개월→2개월, 수수료도 확 줄인다"](https://www.newsis.com/view/NISX20240425_0002712629)
- **진입장벽 체감**: 국내 SaaS 기업 1,100여개 중 CSAP를 취득해 공공에 진출한 곳은 **10% 미만**으로 추정됨 — 스타트업 단계에서는 상당한 자금·시간 부담.
  - 출처: [디지털투데이](https://www.digitaltoday.co.kr/news/articleView.html?idxno=508942)
- **담당 기관**: 과학기술정보통신부, 한국인터넷진흥원(KISA)이 운영.

### 5.3 에듀테크 소프트랩(KERIS)

- 교육부 산하 KERIS(한국교육학술정보원)가 운영하는 제도로, **학교 현장(교사)과 에듀테크 기업을 연결**해 실증(효과성 검증) 프로그램을 진행.
  - 출처: [KERIS 에듀테크 소프트랩](https://www.keris.or.kr/main/cm/cntnts/cntntsViewPop.do?cntntsId=1681), [공교육 에듀테크 도입 가이드(2024 개정판)](https://www.keris.or.kr/main/ad/pblcte/selectPblcteETCInfo.do?mi=1142&pblcteSeq=13775)
- 현직 교사가 직접 에듀테크의 기능·교육적 효과성을 검증하는 실증 프로그램이며, 참여 기업 서비스는 에듀테크 정보 플랫폼 **에듀집(Edujip)**에 등재됨.
- 지역별 소프트랩(경기·충북·서울 등)이 별도 운영되며 매년 참여기업을 공모.
  - 출처: [경기에듀테크소프트랩](https://www.edutechlab.kr:45776), [충북에듀테크소프트랩](https://www.cbedutech.or.kr/)
- 실제 사례로 엘리스그룹이 서울·충북 소프트랩 실증사업에 참여한 바 있음.
  - 출처: [beSUCCESS "엘리스그룹, 에듀테크 소프트랩 실증사업 서울 충북 참여 기업 선정"](https://besuccess.com/?p=183123)
- **소프트랩 참여가 학교 조달에 실질적으로 도움이 되는지(정량적 전환율 등)**: 이번 조사에서 정량 데이터는 **미확인**. 다만 "교사 검증 + 에듀집 등재"라는 구조 자체가 학교의 신뢰 확보·발견 가능성을 높이는 경로로 작동한다는 점은 확인됨.

### 5.4 학교 조달 경로

- **나라장터(G2B)와는 별도로, 교육기관은 S2B(학교장터)를 통해 조달**하는 것이 일반적. S2B에는 교육기관 등 **1만7,000여 곳**이 가입되어 있고, 2022년 기준 조달건수 91만 건, 조달금액 **1조1,855억원** 규모.
  - 출처: [전자신문 "학교장터 수의 계약 1억원으로 올렸는데…학교는 달라진 게 없다"](https://www.etnews.com/20231218000218)
- **에듀테크 카테고리 신설**: 교육부가 디지털 교육 혁신 환경 조성을 위해 S2B 시스템을 개편하며 제품 구분에 **'에듀테크' 카테고리를 신설**(개편 시점: 관련 기사 기준 4월, 연도는 기사 원문상 명확한 연도 표기 재확인 필요 — 사실상 최근 정책, 정확한 연도는 **미확인**으로 표기).
- **수의계약 상한 상향**: 행정안전부 고시 개정과 함께 학교장터 수의계약 상한이 물품 7,000만원→1억원, **용역은 2,000만원 그대로**(에듀테크 소프트웨어는 대부분 '용역'으로 분류되어 여전히 2,000만원 이하에서만 수의계약 가능한 것이 현실적 제약)로 상향/유지.
  - 출처: [전자신문](https://www.etnews.com/20231218000218)
- **시사점**: 소프트웨어(SaaS) 형태 에듀테크는 '용역' 분류상 수의계약 한도가 낮아, 대규모 교육청 단위 계약이 아니라면 **개별 학교 단위 소액 계약(2,000만원 이하) 경로**가 현실적인 초기 진입 채널로 보임. 다만 이는 이번 조사에서 확인된 사실을 바탕으로 한 조사자의 해석이며, 실제 계약 사례 인터뷰 등으로 검증 필요.

---

## 조사 한계 및 후속 확인 필요 항목

- 국내 K-12 코딩교육 전용 시장 규모의 **공신력 있는 1차 출처**(NIPA/한국에듀테크산업협회/통계청 등 정부·협회 공식 발표) — 미확인, 후속 조사 필요.
- 코드모스·코딩앤플레이·하이클래스 등의 **구체적 가격/요금제** — 대부분 공개 정보로 확인 불가, 직접 문의 필요.
- 학교-에듀테크 업체 간 **개인정보 위탁처리 표준계약서/가이드라인**(교육부 또는 개인정보보호위원회 공식본) 존재 여부 — 미확인.
- S2B '에듀테크' 카테고리 신설의 **정확한 시행 연도** — 미확인(기사 원문상 재확인 필요).
- Entry의 "엔트리" 명칭·로고 자체에 대한 **별도 상표 정책 문서** — 미확인(entryjs 라이선스는 Apache 2.0으로 확인했으나 브랜드명 사용 가능 여부는 별도 확인 필요).
- 엔트리의 초등 실과 **검인정 교과서 공식 채택 여부**(교육부/한국검인정교과서협회 공식 문서 기준) — playentry.org의 출판사 연계 페이지 존재만 확인, 공식 채택 여부는 미확인.
