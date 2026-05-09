import os
import re

file_path = '/Users/apple/Desktop/A/coloso/light-coaching/light-coaching-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Sidebar Replacement
old_sidebar = '''      <div class="sb-sec-label">2주차 — 바이브코딩</div>
      <div class="sb-item" data-page="step7" onclick="goPage(this)"><div class="sb-dot"></div>STEP 7. 프롬프트 변환</div>
      <div class="sb-item" data-page="step8" onclick="goPage(this)"><div class="sb-dot"></div>STEP 8. 핵심 기능 실행</div>
      <div class="sb-item" data-page="step9" onclick="goPage(this)"><div class="sb-dot"></div>STEP 9. AI 업무일지 생성</div>
      <div class="sb-item" data-page="step10" onclick="goPage(this)"><div class="sb-dot"></div>STEP 10. 캘린더/통계 추가</div>
      <div class="sb-item" data-page="step11" onclick="goPage(this)"><div class="sb-dot"></div>STEP 11. UX 점검</div>
      <div class="sb-item" data-page="step12" onclick="goPage(this)"><div class="sb-dot"></div>STEP 12. 개선 + 회고</div>
      <div class="sb-item" data-page="mission2" onclick="goPage(this)"><div class="sb-dot"></div>최종 제출</div>
      <div class="sb-divider"></div>'''

new_sidebar = '''      <div class="sb-sec-label">2주차 — 대시보드 MVP 만들기</div>
      <div class="sb-item" data-page="step7" onclick="goPage(this)"><div class="sb-dot"></div>STEP 7. PRD를 구현 프롬프트로 바꾸기</div>
      <div class="sb-item" data-page="step8" onclick="goPage(this)"><div class="sb-dot"></div>STEP 8. 업무 입력/완료 체크 기능 만들기</div>
      <div class="sb-item" data-page="step9" onclick="goPage(this)"><div class="sb-dot"></div>STEP 9. 업무일지 생성 기능 만들기</div>
      <div class="sb-item" data-page="step10" onclick="goPage(this)"><div class="sb-dot"></div>STEP 10. 저장 기능과 기본 UX 점검</div>
      <div class="sb-item" data-page="step11" onclick="goPage(this)"><div class="sb-dot"></div>STEP 11. 오류 수정 및 사용성 개선</div>
      <div class="sb-item" data-page="step12" onclick="goPage(this)"><div class="sb-dot"></div>STEP 12. 최종 제출 및 회고</div>
      <div class="sb-divider"></div>
      <div class="sb-sec-label">BONUS — 선택 확장</div>
      <div class="sb-item" data-page="bonus1" onclick="goPage(this)"><div class="sb-dot"></div>BONUS 1. 캘린더 기능 추가</div>
      <div class="sb-item" data-page="bonus2" onclick="goPage(this)"><div class="sb-dot"></div>BONUS 2. 통계 기능 추가</div>
      <div class="sb-item" data-page="bonus3" onclick="goPage(this)"><div class="sb-dot"></div>BONUS 3. AI 문장 고도화</div>
      <div class="sb-item" data-page="bonus4" onclick="goPage(this)"><div class="sb-dot"></div>BONUS 4. 디자인 커스텀</div>
      <div class="sb-divider"></div>'''

content = content.replace(old_sidebar, new_sidebar)

# 2. Orientation text
content = content.replace(
'''        <div class="page-title">코칭 시작 전에 꼭 읽어주세요 👋</div>
        <div class="page-desc">2주 동안 무엇을 배우는지, 어떤 흐름으로 진행되는지, 슬랙은 어떻게 쓰는지 안내합니다.</div>''',
'''        <div class="page-title">코칭 시작 전에 꼭 읽어주세요 👋</div>
        <div class="page-desc">2주 동안 무엇을 배우는지, 어떤 흐름으로 진행되는지, 슬랙은 어떻게 쓰는지 안내합니다.<br><br>
        이 과정의 필수 완성 목표는 ‘업무 대시보드 MVP’입니다.<br>
        2주 동안 업무 입력, 완료 체크, 업무일지 생성, 기본 저장 기능이 작동하는 첫 번째 버전을 완성합니다.<br>
        캘린더와 통계 기능은 모든 수강생의 필수 과제가 아니라, 기본 기능을 완성한 뒤 더 확장해보고 싶은 분들을 위한 선택 기능으로 제공합니다.<br><br>
        중요한 것은 모든 기능을 다 넣는 것이 아니라, 문제정의에서 출발해 실제로 작동하는 첫 버전을 완성해보는 것입니다.<br>
        기능이 적더라도 사용 흐름이 명확하고, 내가 왜 이 기능을 만들었는지 설명할 수 있다면 이 과정의 핵심 목표는 달성한 것입니다.</div>'''
)

content = content.replace(
'''        <div class="sec">
          <div class="sec-title">2주 후 완성할 앱 — 먼저 보세요</div>''',
'''        <div class="sec">
          <div class="sec-title">필수 MVP 기능 vs 선택 확장 기능</div>
          <div class="info-box">
            <p><b>필수 MVP 기능:</b></p>
            <ul style="margin-left: 20px; color: var(--sub); line-height: 1.8; margin-top: 4px;">
              <li>업무 입력</li>
              <li>업무 수정/삭제</li>
              <li>완료 체크</li>
              <li>완료된 업무 목록 확인</li>
              <li>완료된 업무를 바탕으로 업무일지 생성</li>
              <li>새로고침해도 기록이 유지되는 기본 저장 기능</li>
              <li>오늘 업무 / 완료 업무 / 업무일지 영역이 구분된 기본 대시보드 화면</li>
            </ul>
            <p style="margin-top: 12px;"><b>선택 확장 기능:</b></p>
            <ul style="margin-left: 20px; color: var(--sub); line-height: 1.8; margin-top: 4px;">
              <li>날짜별 기록을 보는 캘린더</li>
              <li>완료율, 카테고리별 업무량, 주간 업무량을 보는 통계</li>
              <li>Ollama 또는 AI 모델을 활용한 업무일지 문장 고도화</li>
              <li>브랜드 컬러, 카드 스타일, 레이아웃 디자인 커스텀</li>
            </ul>
          </div>
        </div>

        <div class="sec">
          <div class="sec-title">2주 후 완성할 앱 — 먼저 보세요</div>'''
)

# 3. Step 6-B and Step 7 reconstruction
# Step 6-B currently ends with Antigravity instructions. We need to split it.
# Let's find step 6-B end nav and the next step
step6b_antigravity = '''        <div class="sec">
          <div class="sec-title">Antigravity 시작 순서</div>
          <div class="step-list">
            <div class="step-card"><div class="step-num g">1</div><div class="step-content"><div class="step-card-title">antigravity.google 접속 → New Project</div><div class="step-card-desc">빈 프로젝트 선택. 템플릿 없이 시작합니다.</div></div></div>
            <div class="step-card"><div class="step-num g">2</div><div class="step-content"><div class="step-card-title">모델 선택 — Gemini 3 Flash 확인</div><div class="step-card-desc">우측 상단 모델 선택에서 <b>Gemini 3 Flash</b>를 선택하세요. 이 모델로 무료 사용이 가능합니다.</div></div></div>
            <div class="step-card"><div class="step-num g">3</div><div class="step-content"><div class="step-card-title">아래 프롬프트 붙여넣기 → 실행</div><div class="step-card-desc">노란 부분을 내 PRD Lite 내용으로 바꾼 뒤 입력창에 붙여넣고 실행하세요.</div></div></div>
          </div>
        </div>'''

# Replace step 6B content: keep only Ollama part.
content = content.replace(step6b_antigravity, '')

# We also need to extract STEP 7 part from step 6b's div
# Currently, step 7 is inside step 6b div! Yes, look at the HTML:
# The `div id="page-step6b"` closes right before `<!-- ══ STEP 8 ══ -->`.
# The nav for step 6b is:
#         <div class="page-nav">
#           <button class="nav-btn" onclick="goPageById('mission1')">← 1주차 미션</button>
#           <button class="nav-btn primary" onclick="goPageById('step8')">STEP 8 — 핵심 기능 실행 →</button>
#         </div>

# Let's cleanly separate page-step6b and create page-step7.
step7_content = '''      <div class="page" id="page-step7">
        <div class="week-badge badge-w2">2주차 · STEP 7</div>
        <div class="context-banner">💡 2주차부터는 결과물이 사람마다 달라질 수 있습니다.<br>AI 코딩 도구는 같은 프롬프트를 입력해도 환경과 이전 코드 상태에 따라 결과가 달라질 수 있습니다.<br>그래서 이 과정에서는 ‘정답 코드’를 외우는 것이 아니라, 원하는 결과를 설명하고, 오류를 좁히고, 기능을 하나씩 완성하는 방식을 연습합니다.</div>
        <div class="page-title">PRD를 구현 프롬프트로 바꾸기</div>
        <div class="page-desc">Antigravity를 실행하고 PRD를 바탕으로 첫 번째 프롬프트를 작성합니다.</div>

''' + step6b_antigravity + '''

        <div class="sec">
          <div class="sec-title">첫 번째 프롬프트 — 노란 부분만 내 내용으로 바꾸세요</div>
          <div class="prompt-block">
            <div class="prompt-header"><div class="prompt-label">STEP 7 — 전체 앱 구조 생성 프롬프트</div><button class="copy-btn" onclick="copyText(this,'p-step7')">복사하기</button></div>
            <div class="prompt-body" id="p-step7">다음 요구사항에 맞는 웹 앱을 Next.js로 만들어줘.

## 앱 이름
<span class="pm">[내 앱 이름 — 예: WorkLog]</span>

## 앱 목적
<span class="pm">[예: 직장인이 하루 업무를 완료 체크하면 AI가 자동으로 업무일지를 생성해주는 개인용 업무 관리 앱]</span>

## 대상 사용자
<span class="pm">[예: 직장인, 프리랜서, 1인 사업자]</span>

## 첫 버전에 포함할 기능 (Must)
<span class="pm">[예:
- 업무 입력 + 카테고리(프로젝트) 선택
- 완료 체크 (체크 시 완료 목록으로 이동)
- 날짜별 데이터 localStorage 저장
- 완료 업무 기반 업무일지 텍스트 자동 생성 (우측 패널)]</span>

## 포함하지 않을 기능 (Out)
- 로그인 / 회원가입
- 팀 공유, 알림, 모바일 앱

## 화면 구조
<span class="pm">[예: 메인 화면: 좌측에 업무 입력창 + 진행중/완료 목록, 우측에 업무일지 패널
좌측 아이콘 사이드바: 대시보드 / 캘린더 / 통계 아이콘]</span>

## UI 스타일
<span class="pm">[예: 다크 모드, 미니멀, 카테고리별 색상 강조]</span>

## 데이터 저장
localStorage를 사용해서 새로고침 후에도 데이터가 유지되게 해줘.

## 업무일지 생성
완료된 업무 목록을 받아서
"[날짜] 업무일지\\n• 업무명 (카테고리)\\n총 N건 완료"
형태의 텍스트를 생성하는 함수를 만들어줘.
지금은 외부 API 없이 완료 항목을 포맷팅만 하는 방식으로 구현해줘.</div>
          </div>
        </div>

        <div class="mission-box">
          <div class="mission-header"><span class="step-tag tag-mission">STEP 7 미션</span><div class="mission-title">첫 번째 프롬프트 실행 후 슬랙 공유</div></div>
          <div class="mission-items">
            <div class="mission-item"><div class="mission-dot"></div>내 PRD Lite 내용으로 노란 부분 수정 완료</div>
            <div class="mission-item"><div class="mission-dot"></div>Antigravity에서 실행 → 화면 캡처 후 슬랙 공유</div>
            <div class="mission-item"><div class="mission-dot"></div>화면이 안 뜨거나 오류 나면 슬랙 질문 양식으로 질문</div>
          </div>
        </div>
        <div class="page-nav">
          <button class="nav-btn" onclick="goPageById('step6b')">← STEP 6-B</button>
          <button class="nav-btn primary" onclick="goPageById('step8')">STEP 8 — 업무 입력/완료 체크 기능 만들기 →</button>
        </div>
      </div>'''

# Delete step 7 content from step 6b
content = re.sub(r'<div class="sec">\s*<div class="sec-title">첫 번째 프롬프트.*?</div>\s*</div>\s*</div>\s*<div class="mission-box">\s*<div class="mission-header"><span class="step-tag tag-mission">STEP 7 미션.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)

# Fix step 6b's nav
content = content.replace(
'''        <div class="page-nav">
          <button class="nav-btn" onclick="goPageById('mission1')">← 1주차 미션</button>
          <button class="nav-btn primary" onclick="goPageById('step8')">STEP 8 — 핵심 기능 실행 →</button>
        </div>
      </div>''',
'''        <div class="page-nav">
          <button class="nav-btn" onclick="goPageById('mission1')">← 1주차 미션</button>
          <button class="nav-btn primary" onclick="goPageById('step7')">STEP 7 — PRD를 구현 프롬프트로 바꾸기 →</button>
        </div>
      </div>
''' + step7_content
)

# 4. Page titles for Step 8, 9, 10, 11, 12
content = content.replace(
'''        <div class="page-title">핵심 기능 실행 — 대시보드 완성</div>''',
'''        <div class="page-title">업무 입력/완료 체크 기능 만들기</div>'''
)
content = content.replace(
'''        <div class="page-title">AI 업무일지 생성 + Ollama 연동</div>''',
'''        <div class="page-title">업무일지 생성 기능 만들기</div>'''
)

# Move Step 10 to Bonus pages, and make Step 10 about saving and UX
step10_original = '''      <!-- ══ STEP 10 ══ -->
      <div class="page" id="page-step10">
        <div class="week-badge badge-w2">2주차 · STEP 10</div>
        <div class="page-title">캘린더 + 통계 화면 추가</div>
        <div class="page-desc">MVP 대시보드가 잘 작동하면 확장 기능을 붙입니다. 하나씩 순서대로 진행하세요.</div>

        <div class="sec">
          <div class="sec-title">목표 결과물 — 캘린더 화면</div>
          <!-- 이미지 자리: WorkLog 캘린더 화면 스크린샷 -->
          <div class="img-placeholder">
            <div class="img-placeholder-icon">🖼</div>
            <div class="img-placeholder-label">WorkLog 캘린더 화면 스크린샷</div>
            <div class="img-placeholder-desc">월간 달력 + 날짜별 인디케이터 + 우측 해당 일 업무 목록<br>images/worklog-calendar.png</div>
          </div>
        </div>

        <div class="sec">
          <div class="sec-title">캘린더 화면 추가 프롬프트</div>
          <div class="prompt-block">
            <div class="prompt-header"><div class="prompt-label">STEP 10-A — 캘린더</div><button class="copy-btn" onclick="copyText(this,'p-step10a')">복사하기</button></div>
            <div class="prompt-body" id="p-step10a">사이드바에 캘린더 아이콘 메뉴를 추가하고, 캘린더 화면을 만들어줘.

- 월간 달력 (7열 격자, 일/월/화/수/목/금/토)
- 각 날짜 칸에 완료 업무 수 도트 표시 (완료: 초록 / 진행중: 노랑)
- 날짜 클릭 시 우측 패널에 해당 날짜 업무 목록 표시
- 오늘 날짜 테두리 강조
- 좌우 화살표로 이전/다음 달 이동
- localStorage 날짜별 데이터 불러와서 표시</div>
          </div>
        </div>

        <div class="sec">
          <div class="sec-title">목표 결과물 — 통계 화면</div>
          <!-- 이미지 자리: WorkLog 통계 화면 스크린샷 -->
          <div class="img-placeholder">
            <div class="img-placeholder-icon">🖼</div>
            <div class="img-placeholder-label">WorkLog 통계 화면 스크린샷</div>
            <div class="img-placeholder-desc">요약 카드 3개 + 주간 트렌드 막대 차트 + 프로젝트별 도넛 차트<br>images/worklog-stats.png</div>
          </div>
        </div>

        <div class="sec">
          <div class="sec-title">통계 화면 추가 프롬프트</div>
          <div class="prompt-block">
            <div class="prompt-header"><div class="prompt-label">STEP 10-B — 통계</div><button class="copy-btn" onclick="copyText(this,'p-step10b')">복사하기</button></div>
            <div class="prompt-body" id="p-step10b">사이드바에 통계 아이콘 메뉴를 추가하고, 통계 화면을 만들어줘.

- 상단 요약 카드 3개: 주간 완료 업무 수 / 완료율(%) / 주요 프로젝트
- 주간 활동 트렌드: 지난 7일 일별 완료 수 막대 차트 (Recharts)
- 프로젝트별 비중: 카테고리별 도넛 차트 (Recharts)
- 차트 아래 카테고리별 건수 목록
- localStorage 데이터 기반 계산</div>
          </div>
        </div>

        <div class="tip-box">
          <div class="tip-icon">💡</div>
          <div><b>순서 중요:</b> 캘린더 먼저 완성 → 확인 → 통계 추가. 한 번에 요청하면 AI가 놓치는 부분이 생깁니다.</div>
        </div>
        <div class="page-nav">
          <button class="nav-btn" onclick="goPageById('step9')">← STEP 9</button>
          <button class="nav-btn primary" onclick="goPageById('step11')">STEP 11 — UX 점검 →</button>
        </div>
      </div>'''

step10_new = '''      <!-- ══ STEP 10 ══ -->
      <div class="page" id="page-step10">
        <div class="week-badge badge-w2">2주차 · STEP 10</div>
        <div class="page-title">저장 기능과 기본 UX 점검</div>
        <div class="page-desc">새로고침해도 데이터가 유지되는지 확인하고, 기본적인 사용성을 점검합니다.</div>
        <div class="sec">
          <div class="sec-title">확인할 점</div>
          <div class="step-list">
            <div class="step-card"><div class="step-num g">✓</div><div class="step-content"><div class="step-card-title">데이터 유지</div><div class="step-card-desc">업무를 입력하고 F5를 눌러 새로고침했을 때 데이터가 유지되는지 확인합니다.</div></div></div>
            <div class="step-card"><div class="step-num g">✓</div><div class="step-content"><div class="step-card-title">기본 UX</div><div class="step-card-desc">입력 후 입력창이 비워지는지, 엔터를 누르면 추가가 되는지 점검합니다.</div></div></div>
          </div>
        </div>
        <div class="page-nav">
          <button class="nav-btn" onclick="goPageById('step9')">← STEP 9</button>
          <button class="nav-btn primary" onclick="goPageById('step11')">STEP 11 — 오류 수정 및 사용성 개선 →</button>
        </div>
      </div>'''

bonus_pages = '''
      <!-- ══ BONUS 1 ══ -->
      <div class="page" id="page-bonus1">
        <div class="week-badge badge-neutral">BONUS</div>
        <div class="context-banner">💡 여기부터는 필수 과정이 아닙니다.<br>업무 입력, 완료 체크, 업무일지 생성, 저장 기능까지 완성한 분들이 더 확장해볼 수 있는 보너스 실습입니다.<br>캘린더와 통계 기능은 앱의 완성도를 높여주지만, 라이트 코칭의 필수 제출 기준에는 포함되지 않습니다.</div>
        <div class="page-title">캘린더 기능 추가</div>
        <div class="page-desc">날짜별 업무 기록을 한눈에 볼 수 있는 캘린더를 추가합니다.</div>

        <div class="sec">
          <div class="sec-title">목표 결과물 — 캘린더 화면</div>
          <div class="img-placeholder">
            <div class="img-placeholder-icon">🖼</div>
            <div class="img-placeholder-label">WorkLog 캘린더 화면 스크린샷</div>
            <div class="img-placeholder-desc">월간 달력 + 날짜별 인디케이터 + 우측 해당 일 업무 목록<br>images/worklog-calendar.png</div>
          </div>
        </div>

        <div class="sec">
          <div class="sec-title">캘린더 화면 추가 프롬프트</div>
          <div class="prompt-block">
            <div class="prompt-header"><div class="prompt-label">BONUS 1 — 캘린더</div><button class="copy-btn" onclick="copyText(this,'p-bonus1')">복사하기</button></div>
            <div class="prompt-body" id="p-bonus1">사이드바에 캘린더 아이콘 메뉴를 추가하고, 캘린더 화면을 만들어줘.

- 월간 달력 (7열 격자, 일/월/화/수/목/금/토)
- 각 날짜 칸에 완료 업무 수 도트 표시 (완료: 초록 / 진행중: 노랑)
- 날짜 클릭 시 우측 패널에 해당 날짜 업무 목록 표시
- 오늘 날짜 테두리 강조
- 좌우 화살표로 이전/다음 달 이동
- localStorage 날짜별 데이터 불러와서 표시</div>
          </div>
        </div>

        <div class="page-nav">
          <button class="nav-btn" onclick="goPageById('step12')">← STEP 12</button>
          <button class="nav-btn primary" onclick="goPageById('bonus2')">BONUS 2 — 통계 기능 추가 →</button>
        </div>
      </div>

      <!-- ══ BONUS 2 ══ -->
      <div class="page" id="page-bonus2">
        <div class="week-badge badge-neutral">BONUS</div>
        <div class="context-banner">💡 통계 기능은 MVP 이후에 사용자 데이터를 시각적으로 보여주는 좋은 기능입니다.</div>
        <div class="page-title">통계 기능 추가</div>
        <div class="page-desc">데이터를 차트로 요약해서 보여줍니다.</div>

        <div class="sec">
          <div class="sec-title">목표 결과물 — 통계 화면</div>
          <div class="img-placeholder">
            <div class="img-placeholder-icon">🖼</div>
            <div class="img-placeholder-label">WorkLog 통계 화면 스크린샷</div>
            <div class="img-placeholder-desc">요약 카드 3개 + 주간 트렌드 막대 차트 + 프로젝트별 도넛 차트<br>images/worklog-stats.png</div>
          </div>
        </div>

        <div class="sec">
          <div class="sec-title">통계 화면 추가 프롬프트</div>
          <div class="prompt-block">
            <div class="prompt-header"><div class="prompt-label">BONUS 2 — 통계</div><button class="copy-btn" onclick="copyText(this,'p-bonus2')">복사하기</button></div>
            <div class="prompt-body" id="p-bonus2">사이드바에 통계 아이콘 메뉴를 추가하고, 통계 화면을 만들어줘.

- 상단 요약 카드 3개: 주간 완료 업무 수 / 완료율(%) / 주요 프로젝트
- 주간 활동 트렌드: 지난 7일 일별 완료 수 막대 차트 (Recharts)
- 프로젝트별 비중: 카테고리별 도넛 차트 (Recharts)
- 차트 아래 카테고리별 건수 목록
- localStorage 데이터 기반 계산</div>
          </div>
        </div>

        <div class="page-nav">
          <button class="nav-btn" onclick="goPageById('bonus1')">← BONUS 1</button>
          <button class="nav-btn primary" onclick="goPageById('bonus3')">BONUS 3 — AI 문장 고도화 →</button>
        </div>
      </div>

      <!-- ══ BONUS 3 ══ -->
      <div class="page" id="page-bonus3">
        <div class="week-badge badge-neutral">BONUS</div>
        <div class="page-title">AI 문장 고도화</div>
        <div class="page-desc">Ollama 또는 AI 모델을 활용해 업무일지 문장을 더욱 매끄럽고 구체적으로 작성해봅니다. 프롬프트를 세밀하게 조정해보세요.</div>
        <div class="page-nav">
          <button class="nav-btn" onclick="goPageById('bonus2')">← BONUS 2</button>
          <button class="nav-btn primary" onclick="goPageById('bonus4')">BONUS 4 — 디자인 커스텀 →</button>
        </div>
      </div>

      <!-- ══ BONUS 4 ══ -->
      <div class="page" id="page-bonus4">
        <div class="week-badge badge-neutral">BONUS</div>
        <div class="page-title">디자인 커스텀</div>
        <div class="page-desc">브랜드 컬러, 카드 스타일, 레이아웃 등을 나만의 스타일로 변경해보세요.</div>
        <div class="page-nav">
          <button class="nav-btn" onclick="goPageById('bonus3')">← BONUS 3</button>
          <button class="nav-btn primary" onclick="goPageById('faq')">자주 막히는 FAQ →</button>
        </div>
      </div>
'''

content = content.replace(step10_original, step10_new + bonus_pages)

content = content.replace(
'''        <div class="page-title">UX 점검</div>''',
'''        <div class="page-title">오류 수정 및 사용성 개선</div>'''
)

content = content.replace(
'''        <div class="page-title">개선 + 회고</div>''',
'''        <div class="page-title">최종 제출 및 회고</div>'''
)

# Step 12 -> 최종 제출 및 회고
# Step 12 originally had a nav to 'mission2'. We will keep the 'mission2' page for now as part of it, but user mentioned:
# 최종 제출 필수 항목 / 선택 항목
# Let's replace mission2 page content.
mission2_old = '''      <!-- ══ 최종 제출 ══ -->
      <div class="page" id="page-mission2">
        <div class="week-badge badge-w2">2주차 · 최종 제출</div>
        <div class="page-title">최종 미션 제출 🎉</div>
        <div class="page-desc">2주 동안 수고 많으셨습니다. 아래 6가지를 슬랙 채널에 공유해주세요.</div>
        <div class="sec">
          <div class="step-list">
            <div class="step-card"><div class="step-num g">1</div><div class="step-content"><div class="step-card-title">작동하는 앱 링크</div><div class="step-card-desc">Antigravity에서 배포한 URL. 또는 캡처 영상/스크린샷으로 대체 가능.</div></div></div>
            <div class="step-card"><div class="step-num g">2</div><div class="step-content"><div class="step-card-title">문제정의 문장 (STEP 2 최종본)</div></div></div>
            <div class="step-card"><div class="step-num g">3</div><div class="step-content"><div class="step-card-title">PRD Lite (STEP 5 완성본)</div></div></div>
            <div class="step-card"><div class="step-num g">4</div><div class="step-content"><div class="step-card-title">Antigravity에서 사용한 주요 프롬프트</div><div class="step-card-desc">기억나는 것만 공유해도 됩니다.</div></div></div>
            <div class="step-card"><div class="step-num g">5</div><div class="step-content"><div class="step-card-title">UX 점검 체크리스트 결과 + 개선 내용</div></div></div>
            <div class="step-card"><div class="step-num g">6</div><div class="step-content"><div class="step-card-title">회고 문서 (STEP 12 3가지 질문 답변)</div></div></div>
          </div>
        </div>
        <div class="highlight-box">
          <p>라이트 코칭에서 경험한 UX 프로세스를 <b>내 아이디어에 직접 적용</b>하고 싶다면 프리미엄 코칭을 확인해보세요.</p>
          <p style="margin-top:8px">8주 동안 개인 아이디어를 MVP로 완성하는 1:1 코칭입니다.</p>
        </div>
        <div class="page-nav">
          <button class="nav-btn" onclick="goPageById('step12')">← STEP 12</button>
          <div style="font-size:13px;color:var(--green-dk)">완료 후 슬랙으로 제출해주세요 ✓</div>
        </div>
      </div>'''

mission2_new = '''      <!-- ══ 최종 제출 ══ -->
      <div class="page" id="page-mission2">
        <div class="week-badge badge-w2">2주차 · 최종 제출</div>
        <div class="page-title">최종 미션 제출 🎉</div>
        <div class="page-desc">2주 동안 수고 많으셨습니다. 아래 항목들을 슬랙 채널에 공유해주세요.</div>
        <div class="sec">
          <div class="sec-title">최종 제출 필수 항목</div>
          <div class="step-list">
            <div class="step-card"><div class="step-num g">1</div><div class="step-content"><div class="step-card-title">작동하는 업무 대시보드 MVP 링크 또는 화면 캡처</div></div></div>
            <div class="step-card"><div class="step-num g">2</div><div class="step-content"><div class="step-card-title">문제정의 1문장</div></div></div>
            <div class="step-card"><div class="step-num g">3</div><div class="step-content"><div class="step-card-title">PRD Lite 문서</div></div></div>
            <div class="step-card"><div class="step-num g">4</div><div class="step-content"><div class="step-card-title">구현에 사용한 주요 프롬프트</div></div></div>
            <div class="step-card"><div class="step-num g">5</div><div class="step-content"><div class="step-card-title">기본 UX 점검 결과</div></div></div>
            <div class="step-card"><div class="step-num g">6</div><div class="step-content"><div class="step-card-title">짧은 회고</div></div></div>
          </div>
        </div>
        
        <div class="sec">
          <div class="sec-title">최종 제출 선택 항목</div>
          <div class="step-list">
            <div class="step-card"><div class="step-num a">+</div><div class="step-content"><div class="step-card-title">캘린더 기능 추가 여부</div></div></div>
            <div class="step-card"><div class="step-num a">+</div><div class="step-content"><div class="step-card-title">통계 기능 추가 여부</div></div></div>
            <div class="step-card"><div class="step-num a">+</div><div class="step-content"><div class="step-card-title">AI 문장 고도화 여부</div></div></div>
            <div class="step-card"><div class="step-num a">+</div><div class="step-content"><div class="step-card-title">디자인 커스텀 여부</div></div></div>
          </div>
        </div>

        <div class="highlight-box">
          <p>이번 라이트 코칭은 정해진 예제를 따라가며 UX 프로세스와 바이브코딩 흐름을 경험하는 과정입니다.<br>
          만약 이 흐름을 본인의 실제 아이디어, 사업 아이템, 포트폴리오 프로젝트에 적용하고 싶다면 프리미엄 코칭에서 더 깊게 다룰 수 있습니다.</p>
        </div>
        <div class="page-nav">
          <button class="nav-btn" onclick="goPageById('step12')">← STEP 12</button>
          <div style="font-size:13px;color:var(--green-dk)">완료 후 슬랙으로 제출해주세요 ✓</div>
        </div>
      </div>'''

content = content.replace(mission2_old, mission2_new)

# Fix Javascript pages mapping
js_pages_old = "const pages = ['step1','step2','step3','step4','step5','step6','step6b',\\n                   'step7','step8','step9','step10','step11','step12'];"
js_pages_new = "const pages = ['step1','step2','step3','step4','step5','step6','step6b',\\n                   'step7','step8','step9','step10','step11','step12','bonus1','bonus2','bonus3','bonus4'];"
content = content.replace(js_pages_old, js_pages_new)

# Fix previous/next buttons
# In step 7: <button class="nav-btn primary" onclick="goPageById('step8')">STEP 8 — 업무 입력/완료 체크 기능 만들기 →</button>
content = content.replace(
'''          <button class="nav-btn primary" onclick="goPageById('step8')">STEP 8 — 핵심 기능 실행 →</button>''',
'''          <button class="nav-btn primary" onclick="goPageById('step8')">STEP 8 — 업무 입력/완료 체크 기능 만들기 →</button>'''
)
content = content.replace(
'''          <button class="nav-btn primary" onclick="goPageById('step9')">STEP 9 — AI 업무일지 생성 →</button>''',
'''          <button class="nav-btn primary" onclick="goPageById('step9')">STEP 9 — 업무일지 생성 기능 만들기 →</button>'''
)
content = content.replace(
'''          <button class="nav-btn primary" onclick="goPageById('step10')">STEP 10 — 캘린더/통계 추가 →</button>''',
'''          <button class="nav-btn primary" onclick="goPageById('step10')">STEP 10 — 저장 기능과 기본 UX 점검 →</button>'''
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully!")
