import re

with open('light-coaching-v3.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Define the new '시작 전' content (Checklist, Antigravity, and the moved & modified Ollama)
new_pages_content = """
        <!-- ══ 사전 준비 체크리스트 ══ -->
        <div class="page" id="page-prep-checklist">
          <div class="week-badge badge-neutral">시작 전</div>
          <div class="page-title">사전 준비 체크리스트 ☑️</div>
          <div class="page-desc">본격적인 시작 전에 필요한 것들이 모두 준비되었는지 확인하세요.</div>
          <div class="sec">
            <div class="info-box" style="font-size:15px">
              <label style="display:flex; gap:10px; margin-bottom:12px; cursor:pointer"><input type="checkbox"> <span><b>Chrome 브라우저</b>: 모든 실습은 크롬 브라우저에 최적화되어 있습니다.</span></label>
              <label style="display:flex; gap:10px; margin-bottom:12px; cursor:pointer"><input type="checkbox"> <span><b>Antigravity 계정/접속 준비</b>: 2주차 구현 실습에 사용할 AI 코딩 도구입니다.</span></label>
              <label style="display:flex; gap:10px; margin-bottom:12px; cursor:pointer"><input type="checkbox"> <span><b>작업용 폴더 생성</b>: 바탕화면 등에 'WorkLog'라는 이름의 빈 폴더를 만들어주세요.</span></label>
              <label style="display:flex; gap:10px; margin-bottom:12px; cursor:pointer"><input type="checkbox"> <span><b>수업 자료 저장 폴더 생성</b>: 제공되는 템플릿과 이미지 자산을 저장할 폴더입니다.</span></label>
              <label style="display:flex; gap:10px; margin-bottom:12px; cursor:pointer"><input type="checkbox"> <span><a href="https://worklog-ten-chi.vercel.app/" target="_blank" style="color:var(--blue)">완성 예시 앱 확인 ↗</a>: 우리가 최종적으로 만들 앱을 미리 둘러보세요.</span></label>
              <label style="display:flex; gap:10px; margin-bottom:12px; cursor:pointer"><input type="checkbox"> <span><b>슬랙 접속 확인</b>: 질문을 남기고 과제를 제출할 커뮤니티입니다.</span></label>
              <label style="display:flex; gap:10px; cursor:pointer"><input type="checkbox"> <span><b>(선택) Ollama 설치 여부 확인</b>: BONUS 과정인 로컬 AI 연동을 해보고 싶다면 확인하세요.</span></label>
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

        <!-- ══ Ollama 설치 (선택 준비) ══ -->
        <div class="page" id="page-ollama-setup">
          <div class="week-badge badge-neutral">시작 전</div>
          <div class="context-banner">💡 필수 설치가 아닙니다! 기본 MVP는 Ollama 없이도 완성 가능하며, AI 문장 고도화(BONUS 3)에서 활용됩니다.</div>
          <div class="page-title">Ollama 설치 — 선택 준비 (내 컴퓨터 AI)</div>
          <div class="page-desc">인터넷 연결이나 API 요금 없이 내 컴퓨터에서만 작동하는 로컬 AI입니다. BONUS 과정에 도전하실 분들만 설치하세요.</div>

          <div class="sec">
            <div class="sec-title">Ollama가 뭔가요?</div>
            <div class="info-box">
              <p>Ollama는 오픈소스 AI 모델을 내 컴퓨터에서 실행할 수 있게 해주는 도구입니다.</p>
              <p style="margin-top:8px">ChatGPT나 Claude는 인터넷을 통해 외부 서버에 요청합니다. Ollama는 반대로 <b>내 컴퓨터 안에서</b> AI가 돌아갑니다.
                인터넷 없어도 되고, API 비용도 없고, 회사 업무 데이터가 외부로 나가지 않아요.</p>
            </div>
          </div>

          <div class="sec">
            <div class="sec-title">왜 이걸 쓰나요?</div>
            <div class="compare-grid">
              <div class="compare-card" style="border-color:var(--red-bd)">
                <div class="compare-card-label" style="color:var(--red-dk)">외부 AI API (OpenAI 등)</div>
                <div class="compare-card-desc" style="margin-top:8px;color:var(--muted)">
                  ❌ API 키 필요<br>
                  ❌ 요청마다 요금 발생<br>
                  ❌ 업무 데이터 외부 서버로 전송<br>
                  ❌ 인터넷 필요
                </div>
              </div>
              <div class="compare-card" style="border-color:var(--green-bd)">
                <div class="compare-card-label" style="color:var(--green-dk)">Ollama (로컬)</div>
                <div class="compare-card-desc" style="margin-top:8px">
                  ✅ API 키 불필요<br>
                  ✅ 완전 무료<br>
                  ✅ 데이터 내 컴퓨터에만 존재<br>
                  ✅ 인터넷 없어도 작동
                </div>
              </div>
            </div>
          </div>

          <div class="sec">
            <div class="sec-title">설치 순서</div>
            <div class="step-list">
              <div class="step-card">
                <div class="step-num g">1</div>
                <div class="step-content">
                  <div class="step-card-title">Ollama 공식 사이트 접속 → 다운로드</div>
                  <div class="step-card-desc">
                    <a href="https://ollama.com" target="_blank" style="color:var(--blue);font-weight:600">ollama.com</a> 접속 → "Download" 버튼 → 본인 OS(Mac/Windows) 선택 후 설치 파일 다운로드
                  </div>
                </div>
              </div>
              <div class="step-card">
                <div class="step-num g">2</div>
                <div class="step-content">
                  <div class="step-card-title">터미널에서 Ollama 실행 확인</div>
                  <div class="step-card-desc">
                    터미널을 열고 <code style="background:var(--card3);padding:1px 6px;border-radius:4px;font-size:12px">ollama run gemma2:2b</code>를 입력하세요.
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="page-nav">
            <button class="nav-btn" onclick="goPageById('antigravity-setup')">← Antigravity 준비</button>
            <button class="nav-btn primary" onclick="goPageById('slack-guide')">슬랙 질문 양식 →</button>
          </div>
        </div>
"""

# Insert at the spot just before the Slack Question Guide (line 1743 approx)
target_comment = '<!-- ══ 슬랙 질문 양식 ══ -->'
if target_comment in html:
    html = html.replace(target_comment, new_pages_content + '\n        ' + target_comment)

# 2. Delete original incorrectly-positioned Ollama content block (around lines 2631~2707)
# Let's find it safely by searching the ID tag exactly
pattern = re.compile(r'<!-- ══ STEP 7 — Ollama ══ -->.*?<div class="page" id="page-step7">.*?</div>\s*</div>\s*(?=<div class="page" id="page-step7">)', re.DOTALL)
# Actually, let's just grab the specific range for replacement manually if regex is hard.
# Searching explicitly from '<!-- ══ STEP 7 — Ollama ══ -->' to just before the next 'page-step7'
old_ollama_start = html.find('<!-- ══ STEP 7 — Ollama ══ -->')
next_page_step7_start = html.find('<div class="page" id="page-step7">', old_ollama_start + 30)

if old_ollama_start != -1 and next_page_step7_start != -1:
    html = html[:old_ollama_start] + html[next_page_step7_start:]

# 3. Rewrite the content of STEP 7 (which was line 2708, now at top of the remaining content)
new_step7_page = """
        <div class="page" id="page-step7">
          <div class="week-badge badge-w2">2주차 · STEP 7</div>
          <div class="context-banner">💡 2주차부터는 결과물이 사람마다 달라질 수 있습니다.<br>AI 코딩 도구는 같은 프롬프트를 입력해도 환경과 이전 코드 상태에 따라 결과가 달라질 수 있습니다.<br>그래서 이 과정에서는 ‘정답 코드’를 외우는 것이 아니라, 원하는 결과를 설명하고, 오류를 좁히고, 기능을 하나씩 완성하는 방식을 연습합니다.</div>
          
          <div class="page-title">STEP 7. 1주차 MD를 구현용 PRD로 변환하기</div>
          <div class="page-desc">1주차에서 작성한 미션 MD 파일은 바로 구현에 사용할 수 있는 문서라기보다, 기획 초안에 가깝습니다.<br><br>
2주차에서는 이 MD 파일을 먼저 GPTs에 업로드해 Antigravity가 이해하기 쉬운 구현용 PRD Lite로 정리합니다.<br><br>
정리된 PRD Lite를 바탕으로 Antigravity에 첫 구현을 요청하면, 업무 대시보드 MVP를 더 안정적으로 시작할 수 있습니다.</div>

          <div class="sec" style="text-align: center; margin: 40px 0;">
            <a href="https://chatgpt.com/g/g-69ff890d4eb08191aa17657122d8736f-1juca-md-guhyeon-prd-byeonhwanbos" target="_blank" class="nav-btn primary" style="display:inline-block; text-decoration:none; padding: 16px 24px; font-size: 16px; border-radius: 8px; box-shadow: 0 4px 12px rgba(29,161,242,0.2);">1주차 MD → 구현 PRD 변환봇 열기 ↗</a>
          </div>

          <div class="sec">
            <div class="sec-title">변환 및 준비 흐름</div>
            <div class="step-list">
              <div class="step-card">
                <div class="step-num a">1</div>
                <div class="step-content">
                  <div class="step-card-title">미션 MD 다운로드</div>
                  <div class="step-card-desc">우측 패널 상단에서 1주차 미션 MD 파일을 다운로드합니다.</div>
                </div>
              </div>
              <div class="step-card">
                <div class="step-num a">2</div>
                <div class="step-content">
                  <div class="step-card-title">GPTs 변환봇 접속</div>
                  <div class="step-card-desc">위 버튼을 눌러 전용 GPTs에 접속합니다.</div>
                </div>
              </div>
              <div class="step-card">
                <div class="step-num a">3</div>
                <div class="step-content">
                  <div class="step-card-title">MD 파일 업로드</div>
                  <div class="step-card-desc">다운받은 MD 파일을 GPTs 대화창에 드래그하여 업로드합니다.</div>
                </div>
              </div>
              <div class="step-card">
                <div class="step-num a">4</div>
                <div class="step-content">
                  <div class="step-card-title">구현용 PRD Lite 확인</div>
                  <div class="step-card-desc">AI가 구조화해준 구현용 문서를 확인합니다.</div>
                </div>
              </div>
              <div class="step-card">
                <div class="step-num a">5</div>
                <div class="step-content">
                  <div class="step-card-title">중복/오류 내용 정리</div>
                  <div class="step-card-desc">불필요하게 반복된 내용이 있다면 수정합니다.</div>
                </div>
              </div>
              <div class="step-card">
                <div class="step-num a">6</div>
                <div class="step-content">
                  <div class="step-card-title">Antigravity 실행 준비</div>
                  <div class="step-card-desc">최종 PRD Lite와 구현 요청문을 복사하여 Antigravity에 붙여넣을 준비를 합니다.</div>
                </div>
              </div>
            </div>
          </div>

          <div class="page-nav">
            <button class="nav-btn" onclick="goPageById('mission1')">← 1주차 미션 제출</button>
            <button class="nav-btn primary" onclick="goPageById('step8')">STEP 8 — 첫 구현 시작 →</button>
          </div>
        </div>
"""

# Find correct page step 7 bounds to replace it
step7_start = html.find('<div class="page" id="page-step7">')
step7_end = html.find('<div class="page" id="page-step8">')
if step7_start != -1 and step7_end != -1:
    html = html[:step7_start] + new_step7_page + html[step7_end:]

# 4. Fix Orientation forward link to go to new pages first
html = html.replace("goPageById('slack-guide')\">다음 — 슬랙 질문 양식 →", "goPageById('prep-checklist')\">다음 — 사전 준비 체크리스트 →")

# 5. Set ID of existing mission panel
html = html.replace('<div class="mission-panel">', '<div class="mission-panel" id="panel-week1">')

# 6. Add the Panel Week 2 HTML right after Panel Week 1 ends.
# First find panel week 1 end
p1_end_str = '</div><!-- /.body-wrap -->'
new_panel2_content = """
      <!-- 2주차 실행 체크리스트 우측 패널 -->
      <div class="mission-panel" id="panel-week2" style="display:none;">
        <div class="week-badge badge-w2" style="font-size:9px; padding:2px 8px;">2주차 · 실행 체크리스트</div>
        <div class="page-title">구현 실행 체크</div>
        <div class="page-desc">2주차 구현 과정의 진도를 스스로 체크하고 점검합니다.</div>

        <style>
          .chk-sec { margin-bottom: 28px; padding: 16px; background: var(--card2); border-radius: var(--r-md); border: 1px solid var(--border-dk); }
          .chk-title { font-size: 13px; font-weight: 700; color: var(--title); margin-bottom: 12px; display: flex; align-items: center; gap: 6px; border-bottom: 1px solid var(--border-nm); padding-bottom: 8px;}
          .chk-item { display: flex; align-items: flex-start; gap: 8px; font-size: 13px; color: var(--title2); margin-bottom: 8px; cursor: pointer; line-height: 1.5;}
          .chk-item input { margin-top: 3px; }
          .chk-sec.active-sec { border-color: var(--green-bd); box-shadow: 0 0 0 1px var(--green-bg); }
        </style>

        <!-- STEP 7 -->
        <div class="chk-sec" id="chk-s7">
          <div class="chk-title"><span class="step-tag tag-blue">STEP 7</span> 구현용 PRD 준비</div>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>1주차 미션 MD 파일을 다운로드했다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>GPTs에 MD 파일을 업로드했다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>구현용 PRD Lite가 생성되었다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>Must 기능이 너무 많지 않은지 확인했다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>캘린더/통계/AI가 Later로 빠졌는지 확인했다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>Antigravity에 붙여넣을 최종 요청문을 준비했다</span></label>
        </div>

        <!-- STEP 8 -->
        <div class="chk-sec" id="chk-s8">
          <div class="chk-title"><span class="step-tag tag-blue">STEP 8</span> 첫 구현 시작 체크</div>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>Antigravity에서 새 프로젝트를 열었다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>구현용 PRD Lite를 붙여넣었다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>전체 구현 계획을 먼저 확인했다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>업무 입력 기능이 생성되었다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>업무 목록이 화면에 표시된다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>저장 방식이 적용되었다</span></label>
        </div>

        <!-- STEP 9 -->
        <div class="chk-sec" id="chk-s9">
          <div class="chk-title"><span class="step-tag tag-blue">STEP 9</span> 업무 관리 기능 체크</div>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>업무를 추가할 수 있다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>업무를 수정할 수 있다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>업무를 삭제할 수 있다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>완료 체크를 할 수 있다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>완료된 업무가 별도로 보인다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>새로고침 후에도 업무가 남아 있다</span></label>
        </div>

        <!-- STEP 10 -->
        <div class="chk-sec" id="chk-s10">
          <div class="chk-title"><span class="step-tag tag-blue">STEP 10</span> 업무일지 생성 체크</div>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>완료된 업무를 기준으로 업무일지가 생성된다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>완료 업무가 없을 때 안내 문구가 나온다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>생성된 업무일지를 복사할 수 있다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>업무일지 문장이 너무 어색하지 않다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>AI 없이도 기본 템플릿 방식으로 작동한다</span></label>
        </div>

        <!-- STEP 11 -->
        <div class="chk-sec" id="chk-s11">
          <div class="chk-title"><span class="step-tag tag-blue">STEP 11</span> UX 점검 체크</div>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>처음 보는 사람도 어디에 입력할지 알 수 있다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>완료 체크 버튼이 명확하다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>오늘 업무와 완료 업무가 구분된다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>업무일지 생성 위치가 자연스럽다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>불필요한 기능이 너무 많이 들어가지 않았다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>모바일 또는 작은 화면에서 크게 깨지지 않는다</span></label>
        </div>

        <!-- STEP 12 -->
        <div class="chk-sec" id="chk-s12">
          <div class="chk-title"><span class="step-tag tag-mission">STEP 12</span> 최종 제출 체크</div>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>작동 화면 캡처를 준비했다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>구현용 PRD Lite를 저장했다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>사용한 주요 프롬프트를 정리했다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>기본 UX 점검 결과를 작성했다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>짧은 회고를 작성했다</span></label>
          <label class="chk-item"><input type="checkbox" onchange="saveCheck(this)"> <span>선택 확장 여부를 체크했다</span></label>
        </div>

      </div>
    </div><!-- /.body-wrap -->
"""
# Replace end of the wrap to inject the new panel
html = html.replace('      </div>\n    </div><!-- /.body-wrap -->', '      </div>\n' + new_panel2_content)

# 7. Modify `goPage` logic in JavaScript to switch panels and highlight correct checklist
# We find the goPage function and rewrite it.
old_gopage = """    function goPage(el) {
      if (el.classList.contains('locked')) return;
      document.querySelectorAll('.sb-item').forEach(i => i.classList.remove('active'));
      el.classList.add('active');
      document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
      const pageId = el.dataset.page;
      const target = document.getElementById('page-' + pageId);
      if (target) {
        target.classList.add('active');
        document.querySelector('.main').scrollTop = 0;
        localStorage.setItem('lc_last_page', pageId);
      }
    }"""

new_gopage = """    function goPage(el) {
      if (el.classList.contains('locked')) return;
      document.querySelectorAll('.sb-item').forEach(i => i.classList.remove('active'));
      el.classList.add('active');
      document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
      const pageId = el.dataset.page;
      const target = document.getElementById('page-' + pageId);
      if (target) {
        target.classList.add('active');
        document.querySelector('.main').scrollTop = 0;
        localStorage.setItem('lc_last_page', pageId);
      }

      // 우측 패널 토글
      const w2Pages = ['step7', 'step8', 'step9', 'step10', 'step11', 'step12', 'bonus1', 'bonus2', 'bonus3', 'bonus4', 'faq'];
      const p1 = document.getElementById('panel-week1');
      const p2 = document.getElementById('panel-week2');
      if(p1 && p2) {
        if (w2Pages.includes(pageId)) {
          p1.style.display = 'none';
          p2.style.display = 'block';
          // 하이라이트
          document.querySelectorAll('.chk-sec').forEach(s => s.classList.remove('active-sec'));
          if (pageId.startsWith('step')) {
            const num = pageId.replace('step', '');
            const sec = document.getElementById('chk-s' + num);
            if (sec) {
              sec.classList.add('active-sec');
              sec.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
          }
        } else {
          p1.style.display = 'block';
          p2.style.display = 'none';
        }
      }
    }

    // 체크리스트 저장 함수
    function saveCheck(el) {
      const checks = document.querySelectorAll('#panel-week2 input[type="checkbox"]');
      const state = Array.from(checks).map(c => c.checked);
      localStorage.setItem('lc_checks', JSON.stringify(state));
    }

    document.addEventListener('DOMContentLoaded', () => {
      const saved = JSON.parse(localStorage.getItem('lc_checks') || '[]');
      const checks = document.querySelectorAll('#panel-week2 input[type="checkbox"]');
      checks.forEach((c, i) => {
        if (saved[i] !== undefined) c.checked = saved[i];
      });
    });
"""

html = html.replace(old_gopage, new_gopage)

# Finally write the file
with open('light-coaching-v3.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: HTML was successfully updated.")
