import re

file_path = '/Users/apple/Desktop/A/coloso/light-coaching/light-coaching-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. CSS changes for Light/Dark Mode
css_old = '''  /* ── design.md 다크 재해석 토큰 ── */
  :root {
    /* Surface */
    --bg:        #0f1117;   /* BG #F1F2F6 → 다크 */
    --card:      #171b25;   /* White #FFFFFF → 다크 카드 */
    --card2:     #1e2333;   /* 2차 카드 */
    --card3:     #252a3a;   /* 3차 카드 */
    /* Border */
    --border-dk: rgba(255,255,255,0.10); /* Dark Border #E7E8EB */
    --border-nm: rgba(255,255,255,0.07); /* Normal Border #EBEDF3 */
    --border-lt: rgba(255,255,255,0.04); /* Light Border #F8F8F8 */
    /* Typography */
    --title:     #e8eaf0;   /* Title Black #161A1C → 반전 */
    --title2:    #c8ccd8;   /* Title Black2 #26292D → 반전 */
    --sub:       #9aa3b8;   /* Sub title Gray #818496 */
    --muted:     #606880;   /* Dark Gray #A9AEB5 */
    --placeholder:#3d4357;  /* Light Gray #CDD3DB */
    /* Primary */
    --blue:      #4A5CFF;   /* Primary Blue — 그대로 */
    --blue-bg:   rgba(74,92,255,0.12);
    --blue-bd:   rgba(74,92,255,0.28);
    --blue-hover:#5a6bff;
    --yellow:    #FFC300;   /* Primary Yellow — 그대로 */
    --yellow-bg: rgba(255,195,0,0.12);
    --yellow-bd: rgba(255,195,0,0.28);
    /* Secondary (다크 재해석) */
    --green:     #16813B;   --green-lt: #E7F4EB;
    --green-dk:  #22c55e;   --green-bg: rgba(34,197,94,0.10); --green-bd: rgba(34,197,94,0.22);
    --red:       #E4032E;   --red-lt:   #FCE8E5;
    --red-dk:    #f87171;   --red-bg:   rgba(248,113,113,0.10);--red-bd:   rgba(248,113,113,0.22);
    --orange:    #EE9A01;   --orange-bg:rgba(238,154,1,0.12);
    --purple:    #a78bfa;   --purple-bg:rgba(167,139,250,0.10);
    /* Shadow tokens from design.md */
    --shadow-lg: 0 4px 12px 0 rgba(0,0,0,0.40);  /* @@ Shadow — 다크에서 강화 */
    --shadow-sm: 0 2px 4px 0 rgba(0,0,0,0.30);   /* ## Shadow */
    --shadow-xs: 0 4px 12px 0 rgba(0,0,0,0.18);  /* ** Shadow */
    /* Radius scale from design.md */
    --r-xs: 5px;   /* tiny tags */
    --r-sm: 8px;   /* buttons — design.md 기준 */
    --r-md: 12px;  /* cards, panels */
    --r-lg: 18px;  /* configurator panels */
    --r-xl: 28px;  /* spotlight modules */
    --r-pill: 980px;
    /* Layout */
    --sidebar-w: 256px;
    --font-display: 'Inter Tight', 'SF Pro Display', 'Helvetica Neue', sans-serif;
    --font-text:    'Inter', 'SF Pro Text', 'Helvetica Neue', sans-serif;
  }'''

css_new = '''  /* ── Light Mode Tokens (Default) ── */
  :root {
    --bg:        #F1F2F6;
    --card:      #FFFFFF;
    --card2:     #F8F9FB;
    --card3:     #F0F2F5;
    --border-dk: #E7E8EB;
    --border-nm: #EBEDF3;
    --border-lt: #F8F8F8;
    --title:     #161A1C;
    --title2:    #26292D;
    --sub:       #818496;
    --muted:     #A9AEB5;
    --placeholder:#CDD3DB;
    --blue:      #4A5CFF;
    --blue-bg:   rgba(74,92,255,0.08);
    --blue-bd:   rgba(74,92,255,0.15);
    --blue-hover:#3848E6;
    --yellow:    #FFC300;
    --yellow-bg: rgba(255,195,0,0.1);
    --yellow-bd: rgba(255,195,0,0.2);
    --green:     #16813B;   --green-lt: #E7F4EB;
    --green-dk:  #16813B;   --green-bg: rgba(22,129,59,0.08); --green-bd: rgba(22,129,59,0.15);
    --red:       #E4032E;   --red-lt:   #FCE8E5;
    --red-dk:    #E4032E;   --red-bg:   rgba(228,3,46,0.08);--red-bd:   rgba(228,3,46,0.15);
    --orange:    #EE9A01;   --orange-bg:rgba(238,154,1,0.08);
    --purple:    #a78bfa;   --purple-bg:rgba(167,139,250,0.08);
    --shadow-lg: 0 4px 12px 0 rgba(0,0,0,0.06);
    --shadow-sm: 0 2px 4px 0 rgba(0,0,0,0.04);
    --shadow-xs: 0 4px 12px 0 rgba(0,0,0,0.03);
    --r-xs: 5px; --r-sm: 8px; --r-md: 12px; --r-lg: 18px; --r-xl: 28px; --r-pill: 980px;
    --sidebar-w: 256px;
    --font-display: 'Inter Tight', 'SF Pro Display', 'Helvetica Neue', sans-serif;
    --font-text:    'Inter', 'SF Pro Text', 'Helvetica Neue', sans-serif;
  }

  /* ── Dark Mode Tokens ── */
  html[data-theme="dark"] {
    --bg:        #0f1117;
    --card:      #171b25;
    --card2:     #1e2333;
    --card3:     #252a3a;
    --border-dk: rgba(255,255,255,0.10);
    --border-nm: rgba(255,255,255,0.07);
    --border-lt: rgba(255,255,255,0.04);
    --title:     #e8eaf0;
    --title2:    #c8ccd8;
    --sub:       #9aa3b8;
    --muted:     #606880;
    --placeholder:#3d4357;
    --blue:      #4A5CFF;
    --blue-bg:   rgba(74,92,255,0.12);
    --blue-bd:   rgba(74,92,255,0.28);
    --blue-hover:#5a6bff;
    --yellow:    #FFC300;
    --yellow-bg: rgba(255,195,0,0.12);
    --yellow-bd: rgba(255,195,0,0.28);
    --green:     #16813B;   --green-lt: #E7F4EB;
    --green-dk:  #22c55e;   --green-bg: rgba(34,197,94,0.10); --green-bd: rgba(34,197,94,0.22);
    --red:       #E4032E;   --red-lt:   #FCE8E5;
    --red-dk:    #f87171;   --red-bg:   rgba(248,113,113,0.10);--red-bd:   rgba(248,113,113,0.22);
    --orange:    #EE9A01;   --orange-bg:rgba(238,154,1,0.12);
    --purple:    #a78bfa;   --purple-bg:rgba(167,139,250,0.10);
    --shadow-lg: 0 4px 12px 0 rgba(0,0,0,0.40);
    --shadow-sm: 0 2px 4px 0 rgba(0,0,0,0.30);
    --shadow-xs: 0 4px 12px 0 rgba(0,0,0,0.18);
  }
  
  .input-textarea {
    width: 100%; min-height: 80px; padding: 12px 16px;
    background: var(--card3); border: 1px solid var(--border-dk);
    border-radius: var(--r-sm); color: var(--title); font-size: 14px;
    font-family: var(--font-text); outline: none; line-height: 1.6;
    transition: border-color .15s; resize: vertical; margin-top: 8px;
  }
  .input-textarea:focus { border-color: var(--blue); }
'''
if css_old in content:
    content = content.replace(css_old, css_new)

# 2. Logos & Toggle Button
logo_lock_old = '''    <div class="lock-logo">
      <img src="data:image/png;base64,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" alt="똑디" style="height:28px;object-fit:contain;filter:brightness(0) invert(1);">
    </div>'''
logo_lock_new = '''    <div class="lock-logo">
      <img id="lock-logo-img" src="/ddokd_logo.png" alt="똑디" style="height:28px;object-fit:contain;">
      <span style="font-size: 18px; font-weight: 700; color: var(--title); font-family: var(--font-display);">라이트 코칭</span>
    </div>'''
content = content.replace(logo_lock_old, logo_lock_new)

logo_topbar_old = '''    <img src="data:image/png;base64,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" alt="똑디" style="height:22px;object-fit:contain;filter:brightness(0) invert(1);">'''
logo_topbar_new = '''    <div class="topbar-logo" style="display:flex;align-items:center;gap:8px;">
      <img id="topbar-logo-img" src="/ddokd_logo.png" alt="똑디" style="height:22px;object-fit:contain;">
      <span style="font-size: 14px; font-weight: 700; color: var(--title); font-family: var(--font-display);">라이트 코칭</span>
    </div>'''
content = content.replace(logo_topbar_old, logo_topbar_new)

topbar_right_old = '''    <div class="topbar-right">
      <a class="topbar-link preview" href="https://worklog-ten-chi.vercel.app/" target="_blank">완성 예시 보기 ↗</a>
      <a class="topbar-link" href="#" target="_blank">슬랙 채널 →</a>
    </div>'''
topbar_right_new = '''    <div class="topbar-right">
      <button id="theme-toggle" onclick="toggleTheme()" style="background:none;border:none;cursor:pointer;font-size:18px;margin-right:12px;">🌓</button>
      <a class="topbar-link preview" href="https://worklog-ten-chi.vercel.app/" target="_blank">완성 예시 보기 ↗</a>
      <a class="topbar-link" href="#" target="_blank">슬랙 채널 →</a>
    </div>'''
content = content.replace(topbar_right_old, topbar_right_new)

# 3. Iframe Remove
iframe_old = '''          <div style="border:1px solid var(--border-dk);border-radius:var(--r-md);overflow:hidden;box-shadow:var(--shadow-sm);">
            <div style="background:var(--card2);padding:8px 14px;display:flex;align-items:center;gap:8px;border-bottom:1px solid var(--border-nm);">
              <div style="display:flex;gap:5px;">
                <div style="width:10px;height:10px;border-radius:50%;background:#ff5f56"></div>
                <div style="width:10px;height:10px;border-radius:50%;background:#ffbd2e"></div>
                <div style="width:10px;height:10px;border-radius:50%;background:#27c93f"></div>
              </div>
              <span style="font-size:11px;color:var(--muted);margin-left:4px">worklog-ten-chi.vercel.app</span>
              <a href="https://worklog-ten-chi.vercel.app/" target="_blank" style="margin-left:auto;font-size:11px;color:var(--blue);text-decoration:none;font-weight:600">새 탭에서 열기 ↗</a>
            </div>
            <iframe
              src="https://worklog-ten-chi.vercel.app/"
              style="width:100%;height:520px;border:none;display:block;"
              title="WorkLog 완성 앱"
              loading="lazy"
              allow="clipboard-write">
            </iframe>
          </div>
          <div class="img-caption" style="margin-top:8px">iframe이 차단된 경우 상단 "새 탭에서 열기" 버튼을 사용하세요.</div>'''
iframe_new = '''          <div class="img-placeholder" style="padding: 60px 20px;">
            <div class="img-placeholder-icon">🔗</div>
            <div class="img-placeholder-label">WorkLog 완성 앱</div>
            <div class="img-placeholder-desc" style="margin-bottom:16px">새 탭에서 열어 직접 조작해보며 흐름을 경험하세요.</div>
            <a href="https://worklog-ten-chi.vercel.app/" target="_blank" class="btn-primary" style="display:inline-block;width:auto;padding:10px 24px;text-decoration:none;">새 탭에서 열기 ↗</a>
          </div>'''
content = content.replace(iframe_old, iframe_new)

# 4. Step Number Shift
content = content.replace('STEP 12', 'STEP 13')
content = content.replace('step12', 'step13')

content = content.replace('STEP 11', 'STEP 12')
content = content.replace('step11', 'step12')

content = content.replace('STEP 10', 'STEP 11')
content = content.replace('step10', 'step11')

content = content.replace('STEP 9', 'STEP 10')
content = content.replace('step9', 'step10')

content = content.replace('STEP 8', 'STEP 9')
content = content.replace('step8', 'step9')

content = content.replace('STEP 7', 'STEP 8')
content = content.replace('step7', 'step8')

content = content.replace('STEP 6-B', 'STEP 7')
content = content.replace('step6b', 'step7')

# Update specific STEP N titles that got weirdly shifted (e.g., if there were numbers in the text).
# It's safer to only shift the JS array.
content = content.replace("['step1','step2','step3','step4','step5','step6','step6b',\\n                   'step7','step8','step9','step10','step11','step12','bonus1','bonus2','bonus3','bonus4']", "['step1','step2','step3','step4','step5','step6','step7','step8','step9','step10','step11','step12','step13','mission1','bonus1','bonus2','bonus3','bonus4']")
content = content.replace("'step6b':'STEP 6-B',\\n      'mission1':'1주차 미션 제출','step7':'STEP 7','step8':'STEP 8','step9':'STEP 9',\\n      'step10':'STEP 10','step11':'STEP 11','step12':'STEP 12','mission2':'최종 제출',", "'step7':'STEP 7',\\n      'mission1':'1주차 미션 제출','step8':'STEP 8','step9':'STEP 9','step10':'STEP 10',\\n      'step11':'STEP 11','step12':'STEP 12','step13':'STEP 13','mission2':'최종 제출',")

# 5. Add Textareas for Steps 3,4,5,6
# Step 3
content = content.replace(
    '''<div class="sec-title">직접 작성해보기 — 내 앱 흐름 적어보기</div>''',
    '''<div class="sec-title">직접 작성해보기 — 내 앱 흐름 적어보기</div>
          <textarea id="in-step3-flow" class="input-textarea" placeholder="앱 열기 → ..." oninput="saveInput('in-step3-flow')"></textarea>'''
)

# Step 4
content = content.replace(
    '''<div class="sec-title">직접 작성해보기 — 내 앱 기능 분류하기</div>''',
    '''<div class="sec-title">직접 작성해보기 — 내 앱 기능 분류하기</div>
          <div style="margin-bottom:10px;"><div class="sec-title">Must (핵심)</div><textarea id="in-step4-must" class="input-textarea" placeholder="Must 기능" oninput="saveInput('in-step4-must')"></textarea></div>
          <div style="margin-bottom:10px;"><div class="sec-title">Later (나중에)</div><textarea id="in-step4-later" class="input-textarea" placeholder="Later 기능" oninput="saveInput('in-step4-later')"></textarea></div>
          <div style="margin-bottom:10px;"><div class="sec-title">Out (제외)</div><textarea id="in-step4-out" class="input-textarea" placeholder="Out 기능" oninput="saveInput('in-step4-out')"></textarea></div>'''
)

# Step 5
content = content.replace(
    '''<div class="sec-title">직접 작성해보기 — 내 PRD Lite 완성하기</div>''',
    '''<div class="sec-title">직접 작성해보기 — 내 PRD Lite 완성하기</div>
          <textarea id="in-step5-prd" class="input-textarea" placeholder="PRD Lite 내용" style="height:200px;" oninput="saveInput('in-step5-prd')"></textarea>'''
)

# Step 6
content = content.replace(
    '''<div class="sec-title">직접 작성해보기</div>
          <div class="tip-box"><div class="tip-icon">✏️</div><div>내 Must 기능을 기준으로 화면 이름과 역할을 텍스트로 정리해보세요. "왼쪽에 뭐, 오른쪽에 뭐" 수준이면 충분합니다. 1주차 미션 제출 시 한번에 제출합니다.</div></div>''',
    '''<div class="sec-title">직접 작성해보기</div>
          <div class="tip-box"><div class="tip-icon">✏️</div><div>내 Must 기능을 기준으로 화면 이름과 역할을 텍스트로 정리해보세요. "왼쪽에 뭐, 오른쪽에 뭐" 수준이면 충분합니다. 1주차 미션 제출 시 한번에 제출합니다.</div></div>
          <textarea id="in-step6-screen" class="input-textarea" placeholder="예: 대시보드 화면 - 왼쪽 입력창, 오른쪽 일지" oninput="saveInput('in-step6-screen')"></textarea>'''
)

# 6. mission1 page HTML
mission1_html = '''
      <!-- ══ 1주차 미션 제출 ══ -->
      <div class="page" id="page-mission1">
        <div class="week-badge badge-w1">1주차 · 미션 제출</div>
        <div class="page-title">1주차 미션 제출</div>
        <div class="page-desc">지금까지 STEP 2~6에서 작성한 내용들이 모였습니다. 여기서 내용을 수정하거나 마크다운으로 다운로드할 수 있습니다.</div>

        <div class="sec">
          <div class="sec-title">1. 문제정의 (STEP 2)</div>
          <textarea id="m1-pd" class="input-textarea" placeholder="문제정의" oninput="saveInput('m1-pd')"></textarea>
        </div>
        <div class="sec">
          <div class="sec-title">2. 사용자 흐름 (STEP 3)</div>
          <textarea id="m1-flow" class="input-textarea" placeholder="사용자 흐름" oninput="saveInput('m1-flow')"></textarea>
        </div>
        <div class="sec">
          <div class="sec-title">3. 기능 우선순위 (STEP 4)</div>
          <div class="sec-title" style="margin-top:8px">Must</div>
          <textarea id="m1-must" class="input-textarea" oninput="saveInput('m1-must')"></textarea>
          <div class="sec-title" style="margin-top:8px">Later</div>
          <textarea id="m1-later" class="input-textarea" oninput="saveInput('m1-later')"></textarea>
          <div class="sec-title" style="margin-top:8px">Out</div>
          <textarea id="m1-out" class="input-textarea" oninput="saveInput('m1-out')"></textarea>
        </div>
        <div class="sec">
          <div class="sec-title">4. PRD Lite (STEP 5)</div>
          <textarea id="m1-prd" class="input-textarea" style="height:150px;" oninput="saveInput('m1-prd')"></textarea>
        </div>
        <div class="sec">
          <div class="sec-title">5. 화면 구조 (STEP 6)</div>
          <textarea id="m1-screen" class="input-textarea" oninput="saveInput('m1-screen')"></textarea>
        </div>

        <button class="btn-primary" onclick="downloadMission1()">마크다운 다운로드</button>

        <div class="page-nav">
          <button class="nav-btn" onclick="goPageById('step7')">← STEP 7</button>
          <button class="nav-btn primary" onclick="goPageById('step8')">STEP 8 — PRD를 구현 프롬프트로 바꾸기 →</button>
        </div>
      </div>
'''

content = content.replace('''<div class="page" id="page-step8">''', mission1_html + '''      <div class="page" id="page-step8">''')

# 7. JavaScript for theme and inputs
js_code = '''
  // ── 테마 토글 ──
  function toggleTheme() {
    const html = document.documentElement;
    const isDark = html.getAttribute('data-theme') === 'dark';
    const newTheme = isDark ? 'light' : 'dark';
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('lc_theme', newTheme);
    updateLogos(newTheme);
  }
  
  function updateLogos(theme) {
    const lockLogo = document.getElementById('lock-logo-img');
    const topbarLogo = document.getElementById('topbar-logo-img');
    const src = theme === 'dark' ? '/ddokd_logo_white.png' : '/ddokd_logo.png';
    if (lockLogo) lockLogo.src = src;
    if (topbarLogo) topbarLogo.src = src;
  }

  // 초기 테마 설정
  const savedTheme = localStorage.getItem('lc_theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateLogos(savedTheme);

  // ── 인풋 저장/동기화 ──
  function saveInput(id) {
    const el = document.getElementById(id);
    if (!el) return;
    localStorage.setItem('lc_' + id, el.value);
    
    // 미션1 페이지와 동기화
    const map = {
      'in-step3-flow': 'm1-flow',
      'in-step4-must': 'm1-must',
      'in-step4-later': 'm1-later',
      'in-step4-out': 'm1-out',
      'in-step5-prd': 'm1-prd',
      'in-step6-screen': 'm1-screen'
    };
    if (map[id]) {
      const target = document.getElementById(map[id]);
      if (target) target.value = el.value;
      localStorage.setItem('lc_' + map[id], el.value);
    }
  }

  // 문제정의 동기화 훅
  const oldUpdatePD = updatePD;
  updatePD = function() {
    oldUpdatePD();
    const u = document.getElementById('pd-user')?.value.trim() || '___';
    const s = document.getElementById('pd-sit')?.value.trim()  || '___';
    const p = document.getElementById('pd-prob')?.value.trim() || '___';
    const ca= document.getElementById('pd-cause')?.value.trim()|| '___';
    const text = `${u}는 ${s}에서 ${p}를 겪고 있으며, 그 이유는 ${ca} 때문이다.`;
    const m1pd = document.getElementById('m1-pd');
    if (m1pd) { m1pd.value = text; localStorage.setItem('lc_m1-pd', text); }
    
    localStorage.setItem('lc_pd-user', document.getElementById('pd-user')?.value || '');
    localStorage.setItem('lc_pd-sit', document.getElementById('pd-sit')?.value || '');
    localStorage.setItem('lc_pd-prob', document.getElementById('pd-prob')?.value || '');
    localStorage.setItem('lc_pd-cause', document.getElementById('pd-cause')?.value || '');
  }

  document.addEventListener('DOMContentLoaded', () => {
    // 저장된 값 불러오기
    const ids = ['in-step3-flow', 'in-step4-must', 'in-step4-later', 'in-step4-out', 'in-step5-prd', 'in-step6-screen', 'm1-pd', 'm1-flow', 'm1-must', 'm1-later', 'm1-out', 'm1-prd', 'm1-screen', 'pd-user', 'pd-sit', 'pd-prob', 'pd-cause'];
    ids.forEach(id => {
      const val = localStorage.getItem('lc_' + id);
      const el = document.getElementById(id);
      if (el && val) el.value = val;
    });
    if (typeof updatePD === 'function') updatePD();
  });
'''
content = content.replace("  const PASSWORD = '1234';", js_code + "\n  const PASSWORD = '1234';")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated HTML with dark/light mode, logo, iframe fix, step numbering, and mission1 textareas.")
