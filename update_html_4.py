import re

file_path = '/Users/apple/Desktop/A/coloso/light-coaching/light-coaching-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update logo heights to 18px
content = content.replace('height:28px', 'height:18px')
content = content.replace('height:22px', 'height:18px')

# 2. Add mission-panel CSS
mission_css = '''
    .mission-panel {
      width: 380px;
      background: var(--card);
      border-left: 1px solid var(--border-nm);
      flex-shrink: 0;
      overflow-y: auto;
      padding: 32px 24px 60px;
    }
    .mission-panel .sec { margin-bottom: 20px; }
    .mission-panel .sec-title { font-size: 10px; margin-bottom: 6px; }
    .mission-panel .input-textarea { font-size: 12px; min-height: 60px; padding: 10px 12px; }
    .mission-panel .page-title { font-size: 18px; margin-bottom: 6px; }
    .mission-panel .page-desc { font-size: 12px; margin-bottom: 20px; }
    .btn-download {
      width: 100%; padding: 12px 15px; border-radius: var(--r-sm);
      font-size: 13px; font-weight: 600; font-family: var(--font-display);
      text-align: center; cursor: pointer; transition: all .15s;
      border: none; margin-top: 10px;
    }
    .btn-download:disabled {
      background: var(--card3); color: var(--muted); cursor: not-allowed;
    }
    .btn-download:not(:disabled) {
      background: var(--blue); color: #fff;
    }
    .btn-download:not(:disabled):hover { background: var(--blue-hover); }

    @media (max-width: 1100px) {
      .mission-panel { display: none; }
    }
'''
if '.mission-panel {' not in content:
    content = content.replace('::-webkit-scrollbar {', mission_css + '\n    ::-webkit-scrollbar {')

# 3. Sidebar modifications
# Remove mission1 item
content = re.sub(r'<div class="sb-item" data-page="mission1".*?</div>\s*', '', content)
# Update array in JS
content = content.replace("'step13','mission1','bonus1'", "'step13','bonus1'")
content = content.replace("'mission1':'1주차 미션 제출',", "")

# 4. Extract and remove page-mission1 from main
mission1_regex = re.compile(r'<!-- ══ 1주차 미션 제출 ══ -->\s*<div class="page" id="page-mission1">.*?</div>\s*</div>\s*<!-- ══ STEP 8 ══ -->', re.DOTALL)
match = mission1_regex.search(content)
if match:
    mission1_html = match.group(0)
    # Remove from main
    content = content.replace(mission1_html, '<!-- ══ STEP 8 ══ -->')
else:
    print("Could not find page-mission1 block")

# 5. Fix navigation links
content = content.replace('''<button class="nav-btn primary" onclick="goPageById('mission1')">1주차 미션 제출 →</button>''', '''<button class="nav-btn primary" onclick="goPageById('step8')">STEP 8 — PRD를 구현 프롬프트로 바꾸기 →</button>''')
content = content.replace('''<button class="nav-btn" onclick="goPageById('mission1')">← 1주차 미션 제출</button>''', '''<button class="nav-btn" onclick="goPageById('step7')">← STEP 7</button>''')

# 6. Add mission-panel HTML
panel_html = '''
    <!-- 1주차 미션 우측 패널 -->
    <div class="mission-panel">
      <div class="week-badge badge-w1" style="font-size:9px; padding:2px 8px;">1주차 · 미션 제출</div>
      <div class="page-title">1주차 미션 제출</div>
      <div class="page-desc">좌측 스텝에서 작성한 내용이 이곳에 자동으로 모입니다. 모든 항목이 채워지면 다운로드가 가능합니다.</div>

      <div class="sec">
        <div class="sec-title">1. 문제정의 (STEP 2)</div>
        <textarea id="m1-pd" class="input-textarea" placeholder="(STEP 2에서 입력 시 자동 완성)" oninput="checkMissionComplete(); saveInput('m1-pd');"></textarea>
      </div>
      <div class="sec">
        <div class="sec-title">2. 사용자 흐름 (STEP 3)</div>
        <textarea id="m1-flow" class="input-textarea" placeholder="(STEP 3에서 입력 시 자동 완성)" oninput="checkMissionComplete(); saveInput('m1-flow');"></textarea>
      </div>
      <div class="sec">
        <div class="sec-title">3. 기능 우선순위 (STEP 4)</div>
        <div class="sec-title" style="margin-top:8px; color:var(--blue);">Must</div>
        <textarea id="m1-must" class="input-textarea" placeholder="(Must 기능)" oninput="checkMissionComplete(); saveInput('m1-must');"></textarea>
        <div class="sec-title" style="margin-top:8px; color:var(--sub);">Later</div>
        <textarea id="m1-later" class="input-textarea" placeholder="(Later 기능)" oninput="checkMissionComplete(); saveInput('m1-later');"></textarea>
        <div class="sec-title" style="margin-top:8px; color:var(--muted);">Out</div>
        <textarea id="m1-out" class="input-textarea" placeholder="(Out 기능)" oninput="checkMissionComplete(); saveInput('m1-out');"></textarea>
      </div>
      <div class="sec">
        <div class="sec-title">4. PRD Lite (STEP 5)</div>
        <textarea id="m1-prd" class="input-textarea" style="height:120px;" placeholder="(STEP 5에서 입력 시 자동 완성)" oninput="checkMissionComplete(); saveInput('m1-prd');"></textarea>
      </div>
      <div class="sec">
        <div class="sec-title">5. 화면 구조 (STEP 6)</div>
        <textarea id="m1-screen" class="input-textarea" placeholder="(STEP 6에서 입력 시 자동 완성)" oninput="checkMissionComplete(); saveInput('m1-screen');"></textarea>
      </div>

      <button id="btn-download-mission" class="btn-download" onclick="downloadMission1()" disabled>모든 항목을 입력해주세요</button>
    </div>
  </div><!-- /.body-wrap -->
'''
content = content.replace('    </div><!-- /.body-wrap -->', panel_html)

# 7. Add validation JS
validation_js = '''
    // ── 미션 완료 체크 ──
    function checkMissionComplete() {
      const ids = ['m1-pd', 'm1-flow', 'm1-must', 'm1-later', 'm1-out', 'm1-prd', 'm1-screen'];
      let allFilled = true;
      for (let id of ids) {
        const el = document.getElementById(id);
        if (!el || !el.value.trim() || el.value.includes('___')) {
          allFilled = false;
          break;
        }
      }
      const btn = document.getElementById('btn-download-mission');
      if (btn) {
        if (allFilled) {
          btn.disabled = false;
          btn.innerText = 'PRD Lite 초안.md 다운로드';
        } else {
          btn.disabled = true;
          btn.innerText = '모든 항목을 입력해주세요';
        }
      }
    }

    // saveInput 수정 (타이핑 시 체크)
    const oldSaveInput = saveInput;
    saveInput = function(id) {
      oldSaveInput(id);
      checkMissionComplete();
    };

    // DOMContentLoaded 에도 체크 추가
    const oldDOMContent = window.onload; // or just append event listener
    document.addEventListener('DOMContentLoaded', () => {
      setTimeout(checkMissionComplete, 100);
    });
'''
content = content.replace('    // ── 인풋 저장/동기화 ──', validation_js + '\n    // ── 인풋 저장/동기화 ──')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML updated with right mission panel!")
