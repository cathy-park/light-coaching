import re

with open('light-coaching-v3.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Sidebar
sidebar_match = re.search(r'<div class="sidebar">.*?</div>\n\s*<!-- 메인 -->', html, re.DOTALL)
new_sidebar = """<div class="sidebar">
        <div class="sb-sec-label">시작 전</div>
        <div class="sb-item active" data-page="orientation" onclick="goPage(this)">
          <div class="sb-dot active"></div>오리엔테이션
        </div>
        <div class="sb-item" data-page="prep-checklist" onclick="goPage(this)">
          <div class="sb-dot"></div>사전 준비 체크리스트
        </div>
        <div class="sb-item" data-page="antigravity-setup" onclick="goPage(this)">
          <div class="sb-dot"></div>Antigravity 설치 및 접속
        </div>
        <div class="sb-item" data-page="ollama-setup" onclick="goPage(this)">
          <div class="sb-dot"></div>Ollama 설치 — 선택 준비
        </div>
        <div class="sb-item" data-page="slack-guide" onclick="goPage(this)">
          <div class="sb-dot"></div>슬랙 질문 양식
        </div>
        <div class="sb-divider"></div>
        <div class="sb-sec-label">1주차 — UX 설계</div>
        <div class="sb-item" data-page="step1" onclick="goPage(this)">
          <div class="sb-dot"></div>STEP 1. 업무 기록 돌아보기
        </div>
        <div class="sb-item" data-page="step2" onclick="goPage(this)">
          <div class="sb-dot"></div>STEP 2. 문제정의
        </div>
        <div class="sb-item" data-page="step3" onclick="goPage(this)">
          <div class="sb-dot"></div>STEP 3. 사용자 흐름 설계
        </div>
        <div class="sb-item" data-page="step4" onclick="goPage(this)">
          <div class="sb-dot"></div>STEP 4. 기능 우선순위
        </div>
        <div class="sb-item" data-page="step5" onclick="goPage(this)">
          <div class="sb-dot"></div>STEP 5. PRD Lite 작성
        </div>
        <div class="sb-item" data-page="step6" onclick="goPage(this)">
          <div class="sb-dot"></div>STEP 6. 화면 구조 설계
        </div>
        <div class="sb-item" data-page="mission1" onclick="goPage(this)">
          <div class="sb-dot"></div>1주차 미션 제출
        </div>
        <div class="sb-divider"></div>
        <div class="sb-sec-label">2주차 — 대시보드 MVP 만들기</div>
        <div class="sb-item" data-page="step7" onclick="goPage(this)">
          <div class="sb-dot"></div>STEP 7. PRD를 구현 프롬프트로 바꾸기
        </div>
        <div class="sb-item" data-page="step8" onclick="goPage(this)">
          <div class="sb-dot"></div>STEP 8. 업무 입력/완료 체크 기능 만들기
        </div>
        <div class="sb-item" data-page="step9" onclick="goPage(this)">
          <div class="sb-dot"></div>STEP 9. 업무일지 생성 기능 만들기
        </div>
        <div class="sb-item" data-page="step10" onclick="goPage(this)">
          <div class="sb-dot"></div>STEP 10. 저장 기능과 기본 UX 점검
        </div>
        <div class="sb-item" data-page="step11" onclick="goPage(this)">
          <div class="sb-dot"></div>STEP 11. 오류 수정 및 사용성 개선
        </div>
        <div class="sb-item" data-page="step12" onclick="goPage(this)">
          <div class="sb-dot"></div>STEP 12. 최종 제출 및 회고
        </div>
        <div class="sb-divider"></div>
        <div class="sb-sec-label">BONUS — 선택 확장</div>
        <div class="sb-item" data-page="bonus1" onclick="goPage(this)">
          <div class="sb-dot"></div>BONUS 1. 캘린더 기능 추가
        </div>
        <div class="sb-item" data-page="bonus2" onclick="goPage(this)">
          <div class="sb-dot"></div>BONUS 2. 통계 기능 추가
        </div>
        <div class="sb-item" data-page="bonus3" onclick="goPage(this)">
          <div class="sb-dot"></div>BONUS 3. AI 문장 고도화
        </div>
        <div class="sb-item" data-page="bonus4" onclick="goPage(this)">
          <div class="sb-dot"></div>BONUS 4. 디자인 커스텀
        </div>
        <div class="sb-divider"></div>
        <div class="sb-sec-label">참고 자료</div>
        <div class="sb-item" data-page="faq" onclick="goPage(this)">
          <div class="sb-dot"></div>자주 막히는 FAQ
        </div>
      </div>
      <!-- 메인 -->"""
html = html[:sidebar_match.start()] + new_sidebar + html[sidebar_match.end():]

# 2. Modify Orientation
html = html.replace('1주차: UX 설계 (문제정의부터 화면 구조까지) + 로컬 AI 설치<br>', '1주차: UX 설계 (문제정의부터 화면 구조까지)<br>')
html = html.replace('1주차 미션 (기획안 + AI 설치 캡처)', '1주차 미션 (기획안)')
html = html.replace('2주차 필수 기능: 업무 입력, 완료 체크, 저장 기능, 일지 생성', '2주차 대시보드 MVP: 업무 입력, 완료 체크, 저장 기능, 일지 생성')

# 3. Create New Pages and Update Ollama
# Find the end of orientation page
ori_end_match = re.search(r'</div>\s*<!-- ══ 슬랙 ══ -->', html)
if ori_end_match:
    new_pages = """
        <!-- ══ 사전 준비 체크리스트 ══ -->
        <div class="page" id="page-prep-checklist">
          <div class="week-badge badge-neutral">시작 전</div>
          <div class="page-title">사전 준비 체크리스트 ☑️</div>
          <div class="page-desc">본격적인 시작 전에 필요한 것들이 모두 준비되었는지 확인하세요.</div>
          <div class="sec">
            <div class="info-box" style="font-size:15px">
              <label style="display:flex; gap:10px; margin-bottom:12px; cursor:pointer"><input type="checkbox"> <b>Chrome 브라우저</b>: 모든 실습은 크롬 브라우저에 최적화되어 있습니다.</label>
              <label style="display:flex; gap:10px; margin-bottom:12px; cursor:pointer"><input type="checkbox"> <b>Antigravity 계정/접속 준비</b>: 2주차 구현 실습에 사용할 AI 코딩 도구입니다.</label>
              <label style="display:flex; gap:10px; margin-bottom:12px; cursor:pointer"><input type="checkbox"> <b>작업용 폴더 생성</b>: 바탕화면 등에 'WorkLog'라는 이름의 빈 폴더를 만들어주세요.</label>
              <label style="display:flex; gap:10px; margin-bottom:12px; cursor:pointer"><input type="checkbox"> <b>수업 자료 저장 폴더 생성</b>: 제공되는 템플릿과 이미지 자산을 저장할 폴더입니다.</label>
              <label style="display:flex; gap:10px; margin-bottom:12px; cursor:pointer"><input type="checkbox"> <a href="https://worklog-ten-chi.vercel.app/" target="_blank" style="color:var(--blue)">완성 예시 앱 확인 ↗</a>: 우리가 최종적으로 만들 앱을 미리 둘러보세요.</label>
              <label style="display:flex; gap:10px; margin-bottom:12px; cursor:pointer"><input type="checkbox"> <b>슬랙 접속 확인</b>: 질문을 남기고 과제를 제출할 커뮤니티입니다.</label>
              <label style="display:flex; gap:10px; cursor:pointer"><input type="checkbox"> <b>(선택) Ollama 설치 여부 확인</b>: BONUS 과정인 로컬 AI 연동을 해보고 싶다면 확인하세요.</label>
            </div>
          </div>
          <div class="page-nav">
            <button class="nav-btn" onclick="goPageById('orientation')">← 오리엔테이션</button>
            <button class="nav-btn primary" onclick="goPageById('antigravity-setup')">Antigravity 설치 및 접속 →</button>
          </div>
        </div>

        <!-- ══ Antigravity 설치 및 접속 ══ -->
        <div class="page" id="page-antigravity-setup">
          <div class="week-badge badge-neutral">시작 전</div>
          <div class="page-title">Antigravity 설치 및 접속 🚀</div>
          <div class="page-desc">2주차 구현 실습에서 코딩을 대신해 줄 필수 도구입니다.</div>
          
          <div class="sec">
            <div class="sec-title">Antigravity란?</div>
            <div class="info-box">
              우리가 작성한 PRD(제품 요구사항 정의서)를 바탕으로 실제 코드를 작성해주는 AI 코딩 에이전트입니다. 직접 코드를 한 줄씩 타이핑할 필요 없이, 우리가 내리는 명령(프롬프트)에 따라 Antigravity가 앱을 완성해 나갑니다.
            </div>
          </div>

          <div class="sec">
            <div class="sec-title">준비 방법</div>
            <div class="step-list">
              <div class="step-card">
                <div class="step-num g">1</div>
                <div class="step-content">
                  <div class="step-card-title">Antigravity 접속</div>
                  <div class="step-card-desc">안내받은 링크를 통해 Antigravity 환경에 접속합니다.</div>
                </div>
              </div>
              <div class="step-card">
                <div class="step-num g">2</div>
                <div class="step-content">
                  <div class="step-card-title">모델 선택: Gemini 3 Flash</div>
                  <div class="step-card-desc">작업 환경 설정에서 모델을 <b>Gemini 3 Flash</b>로 선택해주세요. 가장 빠르고 안정적인 결과를 얻을 수 있습니다.</div>
                </div>
              </div>
            </div>
          </div>

          <div class="page-nav">
            <button class="nav-btn" onclick="goPageById('prep-checklist')">← 사전 준비 체크리스트</button>
            <button class="nav-btn primary" onclick="goPageById('ollama-setup')">Ollama 설치 — 선택 준비 →</button>
          </div>
        </div>
"""
    html = html[:ori_end_match.start()] + new_pages + html[ori_end_match.start():]

# Move and modify Ollama Setup
ollama_start = html.find('<!-- ══ STEP 7 — Ollama ══ -->')
ollama_end = html.find('<!-- ══ STEP 8 ══ -->')
if ollama_start != -1 and ollama_end != -1:
    ollama_content = html[ollama_start:ollama_end]
    html = html[:ollama_start] + html[ollama_end:] # remove from old position
    
    # modify ollama content
    ollama_content = ollama_content.replace('id="page-step7"', 'id="page-ollama-setup"')
    ollama_content = ollama_content.replace('1주차 · STEP 7', '시작 전')
    ollama_content = ollama_content.replace('Ollama 설치 — 내 컴퓨터에서 돌아가는 AI 엔진', 'Ollama 설치 — 선택 준비 (내 컴퓨터 AI)')
    ollama_content = ollama_content.replace('2주차 STEP 10에서 이 Ollama를 앱에 연결합니다. 지금 설치해두면 2주차가 훨씬 수월해요.', '필수 설치가 아닙니다! 기본 MVP는 Ollama 없이도 완성 가능하며, AI 문장 고도화(BONUS 3)에서 활용됩니다.')
    ollama_content = ollama_content.replace('2주차에서 만들 업무일지 AI 생성 기능의 핵심입니다. API 키 없이, 요금 없이, 내 컴퓨터에서만 작동하는 로컬 AI를 설치합니다.', '인터넷 연결이나 API 요금 없이 내 컴퓨터에서만 작동하는 로컬 AI입니다. BONUS 과정에 도전하실 분들만 설치하세요.')
    ollama_content = ollama_content.replace('<!-- ══ STEP 7 — Ollama ══ -->', '<!-- ══ Ollama ══ -->')
    
    # replace nav buttons in ollama
    nav_match = re.search(r'<div class="page-nav">.*?</div>', ollama_content, re.DOTALL)
    if nav_match:
        new_nav = """<div class="page-nav">
            <button class="nav-btn" onclick="goPageById('antigravity-setup')">← Antigravity 준비</button>
            <button class="nav-btn primary" onclick="goPageById('slack-guide')">슬랙 질문 양식 →</button>
          </div>"""
        ollama_content = ollama_content[:nav_match.start()] + new_nav + ollama_content[nav_match.end():]
        
    # insert before slack guide
    slack_start = html.find('<!-- ══ 슬랙 ══ -->')
    html = html[:slack_start] + ollama_content + html[slack_start:]

# 4. Shift week 2 steps (8~13 -> 7~12)
# We will do this carefully using regex replacements to avoid overlapping.
html = html.replace('goPageById(\'step8\')', 'goPageById(\'step7\')')
html = html.replace('goPageById(\'step9\')', 'goPageById(\'step8\')')
html = html.replace('goPageById(\'step10\')', 'goPageById(\'step9\')')
html = html.replace('goPageById(\'step11\')', 'goPageById(\'step10\')')
html = html.replace('goPageById(\'step12\')', 'goPageById(\'step11\')')
html = html.replace('goPageById(\'step13\')', 'goPageById(\'step12\')')

# Update page IDs
html = html.replace('id="page-step8"', 'id="page-step7"')
html = html.replace('id="page-step9"', 'id="page-step8"')
html = html.replace('id="page-step10"', 'id="page-step9"')
html = html.replace('id="page-step11"', 'id="page-step10"')
html = html.replace('id="page-step12"', 'id="page-step11"')
html = html.replace('id="page-step13"', 'id="page-step12"')

# Update step titles/badges
html = html.replace('STEP 8 — ', 'STEP 7 — ')
html = html.replace('STEP 9 — ', 'STEP 8 — ')
html = html.replace('STEP 10 — ', 'STEP 9 — ')
html = html.replace('STEP 11 — ', 'STEP 10 — ')
html = html.replace('STEP 12 — ', 'STEP 11 — ')
html = html.replace('STEP 13 — ', 'STEP 12 — ')
html = html.replace('STEP 8', 'STEP 7')
html = html.replace('STEP 9', 'STEP 8')
html = html.replace('STEP 10', 'STEP 9')
html = html.replace('STEP 11', 'STEP 10')
html = html.replace('STEP 12', 'STEP 11')
html = html.replace('STEP 13', 'STEP 12')

# Note: The above might replace "STEP 8" to "STEP 7" inside the text properly, 
# but it also changes "STEP 13" to "STEP 12".

# Remove Ollama from Step 6 Mission
html = html.replace('<div class="mission-item">\n                <div class="mission-dot"></div>Ollama 설치 + 테스트 캡처 (STEP 7)\n              </div>', '')

# Remove step 6 next button to point to step 7? No, week 1 ends at step 6, so step 6 next button should point to something else? Actually, week 1 has mission1, but mission1 is just a submission panel? Wait, step 6 next should be 'mission1'? No, 'mission1' page doesn't exist. There is a right panel for mission1. So what is the next step after step 6?
# In the original, step 6 -> step 7 -> step 8. Now it's step 6 -> step 7 (which is week 2).
html = html.replace('onclick="goPageById(\'step7\')">STEP 7 — Ollama 설치 →</button>', 'onclick="goPageById(\'step7\')">STEP 7 — PRD를 구현 프롬프트로 바꾸기 →</button>')

# 5. Fix JS Pages list
js_match = re.search(r"const pages = \['step1'.*?\];", html, re.DOTALL)
if js_match:
    html = html[:js_match.start()] + "const pages = ['orientation', 'prep-checklist', 'antigravity-setup', 'ollama-setup', 'slack-guide', 'step1', 'step2', 'step3', 'step4', 'step5', 'step6', 'step7', 'step8', 'step9', 'step10', 'step11', 'step12', 'bonus1', 'bonus2', 'bonus3', 'bonus4', 'faq'];" + html[js_match.end():]

# Fix script variable pageTitles
pt_match = re.search(r"const pageTitles = \{.*?\}\);", html, re.DOTALL)
if pt_match:
    new_pt = """const pageTitles = {
      'orientation': '오리엔테이션', 'prep-checklist': '사전 준비 체크리스트', 'antigravity-setup': 'Antigravity 설치 및 접속', 'ollama-setup': 'Ollama 설치', 'slack-guide': '슬랙 질문 양식',
      'step1': 'STEP 1', 'step2': 'STEP 2', 'step3': 'STEP 3',
      'step4': 'STEP 4', 'step5': 'STEP 5', 'step6': 'STEP 6',
      'step7': 'STEP 7', 'step8': 'STEP 8', 'step9': 'STEP 9',
      'step10': 'STEP 10', 'step11': 'STEP 11', 'step12': 'STEP 12',
      'bonus1': 'BONUS 1', 'bonus2': 'BONUS 2', 'bonus3': 'BONUS 3', 'bonus4': 'BONUS 4', 'faq': 'FAQ'
    };"""
    # Just replacing the object definition inside it
    html = html.replace(pt_match.group(), new_pt + '\n    document.addEventListener("DOMContentLoaded", () => {')

# Also, update step 6 next button properly since we changed 'STEP 7' replacements.
html = html.replace('← STEP 6</button>', '← STEP 6</button>')

# Fix "2주차 확장" to "BONUS 선택 확장"
html = html.replace('2주차 확장', 'BONUS 선택 확장')

with open('light-coaching-v3.html', 'w', encoding='utf-8') as f:
    f.write(html)
