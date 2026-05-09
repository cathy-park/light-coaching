import re

file_path = '/Users/apple/Desktop/A/coloso/light-coaching/light-coaching-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS: Replace :root with dark mode tokens and remove html[data-theme="dark"]
css_old = '''    /* ── Light Mode Tokens (Default) ── */
    :root {
      --bg: #F1F2F6;
      --card: #FFFFFF;
      --card2: #F8F9FB;
      --card3: #F0F2F5;
      --border-dk: #E7E8EB;
      --border-nm: #EBEDF3;
      --border-lt: #F8F8F8;
      --title: #161A1C;
      --title2: #26292D;
      --sub: #818496;
      --muted: #A9AEB5;
      --placeholder: #CDD3DB;
      --blue: #4A5CFF;
      --blue-bg: rgba(74, 92, 255, 0.08);
      --blue-bd: rgba(74, 92, 255, 0.15);
      --blue-hover: #3848E6;
      --yellow: #FFC300;
      --yellow-bg: rgba(255, 195, 0, 0.1);
      --yellow-bd: rgba(255, 195, 0, 0.2);
      --green: #16813B;
      --green-lt: #E7F4EB;
      --green-dk: #16813B;
      --green-bg: rgba(22, 129, 59, 0.08);
      --green-bd: rgba(22, 129, 59, 0.15);
      --red: #E4032E;
      --red-lt: #FCE8E5;
      --red-dk: #E4032E;
      --red-bg: rgba(228, 3, 46, 0.08);
      --red-bd: rgba(228, 3, 46, 0.15);
      --orange: #EE9A01;
      --orange-bg: rgba(238, 154, 1, 0.08);
      --purple: #a78bfa;
      --purple-bg: rgba(167, 139, 250, 0.08);
      --shadow-lg: 0 4px 12px 0 rgba(0, 0, 0, 0.06);
      --shadow-sm: 0 2px 4px 0 rgba(0, 0, 0, 0.04);
      --shadow-xs: 0 4px 12px 0 rgba(0, 0, 0, 0.03);
      --r-xs: 5px;
      --r-sm: 8px;
      --r-md: 12px;
      --r-lg: 18px;
      --r-xl: 28px;
      --r-pill: 980px;
      --sidebar-w: 256px;
      --font-display: 'Inter Tight', 'SF Pro Display', 'Helvetica Neue', sans-serif;
      --font-text: 'Inter', 'SF Pro Text', 'Helvetica Neue', sans-serif;
    }

    /* ── Dark Mode Tokens ── */
    html[data-theme="dark"] {
      --bg: #0f1117;
      --card: #171b25;
      --card2: #1e2333;
      --card3: #252a3a;
      --border-dk: rgba(255, 255, 255, 0.10);
      --border-nm: rgba(255, 255, 255, 0.07);
      --border-lt: rgba(255, 255, 255, 0.04);
      --title: #e8eaf0;
      --title2: #c8ccd8;
      --sub: #9aa3b8;
      --muted: #606880;
      --placeholder: #3d4357;
      --blue: #4A5CFF;
      --blue-bg: rgba(74, 92, 255, 0.12);
      --blue-bd: rgba(74, 92, 255, 0.28);
      --blue-hover: #5a6bff;
      --yellow: #FFC300;
      --yellow-bg: rgba(255, 195, 0, 0.12);
      --yellow-bd: rgba(255, 195, 0, 0.28);
      --green: #16813B;
      --green-lt: #E7F4EB;
      --green-dk: #22c55e;
      --green-bg: rgba(34, 197, 94, 0.10);
      --green-bd: rgba(34, 197, 94, 0.22);
      --red: #E4032E;
      --red-lt: #FCE8E5;
      --red-dk: #f87171;
      --red-bg: rgba(248, 113, 113, 0.10);
      --red-bd: rgba(248, 113, 113, 0.22);
      --orange: #EE9A01;
      --orange-bg: rgba(238, 154, 1, 0.12);
      --purple: #a78bfa;
      --purple-bg: rgba(167, 139, 250, 0.10);
      --shadow-lg: 0 4px 12px 0 rgba(0, 0, 0, 0.40);
      --shadow-sm: 0 2px 4px 0 rgba(0, 0, 0, 0.30);
      --shadow-xs: 0 4px 12px 0 rgba(0, 0, 0, 0.18);
    }'''
css_new = '''    /* ── Dark Mode Tokens (Default) ── */
    :root {
      --bg: #0f1117;
      --card: #171b25;
      --card2: #1e2333;
      --card3: #252a3a;
      --border-dk: rgba(255, 255, 255, 0.10);
      --border-nm: rgba(255, 255, 255, 0.07);
      --border-lt: rgba(255, 255, 255, 0.04);
      --title: #e8eaf0;
      --title2: #c8ccd8;
      --sub: #9aa3b8;
      --muted: #606880;
      --placeholder: #3d4357;
      --blue: #4A5CFF;
      --blue-bg: rgba(74, 92, 255, 0.12);
      --blue-bd: rgba(74, 92, 255, 0.28);
      --blue-hover: #5a6bff;
      --yellow: #FFC300;
      --yellow-bg: rgba(255, 195, 0, 0.12);
      --yellow-bd: rgba(255, 195, 0, 0.28);
      --green: #16813B;
      --green-lt: #E7F4EB;
      --green-dk: #22c55e;
      --green-bg: rgba(34, 197, 94, 0.10);
      --green-bd: rgba(34, 197, 94, 0.22);
      --red: #E4032E;
      --red-lt: #FCE8E5;
      --red-dk: #f87171;
      --red-bg: rgba(248, 113, 113, 0.10);
      --red-bd: rgba(248, 113, 113, 0.22);
      --orange: #EE9A01;
      --orange-bg: rgba(238, 154, 1, 0.12);
      --purple: #a78bfa;
      --purple-bg: rgba(167, 139, 250, 0.10);
      --shadow-lg: 0 4px 12px 0 rgba(0, 0, 0, 0.40);
      --shadow-sm: 0 2px 4px 0 rgba(0, 0, 0, 0.30);
      --shadow-xs: 0 4px 12px 0 rgba(0, 0, 0, 0.18);
      --r-xs: 5px;
      --r-sm: 8px;
      --r-md: 12px;
      --r-lg: 18px;
      --r-xl: 28px;
      --r-pill: 980px;
      --sidebar-w: 256px;
      --font-display: 'Inter Tight', 'SF Pro Display', 'Helvetica Neue', sans-serif;
      --font-text: 'Inter', 'SF Pro Text', 'Helvetica Neue', sans-serif;
    }'''

if css_old in content:
    content = content.replace(css_old, css_new)

# 2. Fix Logos and Remove Toggle Button
logo_lock_old = '''<img id="lock-logo-img" src="/ddokd_logo.png" alt="똑디" style="height:28px;object-fit:contain;">'''
logo_lock_new = '''<img id="lock-logo-img" src="ddokd_logo_white.png" alt="똑디" style="height:28px;object-fit:contain;">'''
content = content.replace(logo_lock_old, logo_lock_new)

logo_topbar_old = '''<img id="topbar-logo-img" src="/ddokd_logo.png" alt="똑디" style="height:22px;object-fit:contain;">'''
logo_topbar_new = '''<img id="topbar-logo-img" src="ddokd_logo_white.png" alt="똑디" style="height:22px;object-fit:contain;">'''
content = content.replace(logo_topbar_old, logo_topbar_new)

btn_old = '''<button id="theme-toggle" onclick="toggleTheme()" style="background:none;border:none;cursor:pointer;font-size:18px;margin-right:12px;">🌓</button>'''
content = content.replace(btn_old, '')

# 3. Remove JS logic for theme
js_old = '''  // ── 테마 토글 ──
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
  updateLogos(savedTheme);'''
content = content.replace(js_old, '')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML updated!")
