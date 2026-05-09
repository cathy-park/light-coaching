import re

file_path = '/Users/apple/Desktop/A/coloso/light-coaching/light-coaching-v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change m1-pd to contenteditable div
old_m1_pd = '<textarea id="m1-pd" class="input-textarea" placeholder="(STEP 2에서 입력 시 자동 완성)"\n            oninput="checkMissionComplete(); saveInput(\'m1-pd\');"></textarea>'
new_m1_pd = '<div id="m1-pd" class="input-textarea" style="white-space:pre-wrap; outline:none; cursor:text; min-height:60px; display:block;" contenteditable="true" placeholder="(STEP 2에서 입력 시 자동 완성)" oninput="checkMissionComplete(); saveInput(\'m1-pd\');"></div>'

if old_m1_pd in content:
    content = content.replace(old_m1_pd, new_m1_pd)
else:
    # Try an alternate format since IDE formatting might differ
    content = re.sub(r'<textarea id="m1-pd"[^>]*></textarea>', new_m1_pd, content)

# To make placeholder work on div
placeholder_css = '''
    .input-textarea[contenteditable]:empty:before {
      content: attr(placeholder);
      color: var(--placeholder);
    }
'''
if 'contenteditable]:empty' not in content:
    content = content.replace('.input-textarea {', placeholder_css + '\n    .input-textarea {')


# 2. Update checkMissionComplete
old_check = '''        const el = document.getElementById(id);
        if (!el || !el.value.trim() || el.value.includes('___')) {'''
new_check = '''        const el = document.getElementById(id);
        const val = el ? (el.value !== undefined ? el.value : el.innerText) : '';
        if (!el || !val.trim() || val.includes('___')) {'''
content = content.replace(old_check, new_check)


# 3. Update saveInput
old_save = '''    function saveInput(id) {
      const el = document.getElementById(id);
      if (!el) return;
      localStorage.setItem('lc_' + id, el.value);'''
new_save = '''    function saveInput(id) {
      const el = document.getElementById(id);
      if (!el) return;
      const val = el.value !== undefined ? el.value : el.innerHTML;
      localStorage.setItem('lc_' + id, val);'''
content = content.replace(old_save, new_save)


# 4. Update updatePD hook
old_hook = '''      const text = `${u}는 ${s}에서 ${p}를 겪고 있으며, 그 이유는 ${ca} 때문이다.`;
      const m1pd = document.getElementById('m1-pd');
      if (m1pd) { m1pd.value = text; localStorage.setItem('lc_m1-pd', text); }'''
new_hook = '''      const user = u || '___';
      const sit = s || '___';
      const prob = p || '___';
      const cause = ca || '___';
      const htmlStr = `<span style="color:#60a5fa;font-weight:600">${user}</span>는 <span style="color:var(--green-dk);font-weight:600">${sit}</span>에서 <span style="color:var(--red-dk);font-weight:600">${prob}</span>를 겪고 있으며, 그 이유는 <span style="color:var(--yellow);font-weight:600">${cause}</span> 때문이다.`;
      const m1pd = document.getElementById('m1-pd');
      if (m1pd) { m1pd.innerHTML = htmlStr; localStorage.setItem('lc_m1-pd', htmlStr); }'''
content = content.replace(old_hook, new_hook)


# 5. Update DOMContentLoaded loader
old_loader = '''        if (el && val) el.value = val;'''
new_loader = '''        if (el && val) {
          if (el.value !== undefined) el.value = val;
          else el.innerHTML = val;
        }'''
content = content.replace(old_loader, new_loader)


# 6. Update downloadMission1
old_dl = '''      const pd = document.getElementById('m1-pd')?.value || '(미작성)';'''
new_dl = '''      const pdEl = document.getElementById('m1-pd');
      const pd = pdEl ? (pdEl.value !== undefined ? pdEl.value : pdEl.innerText) : '(미작성)';'''
content = content.replace(old_dl, new_dl)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates applied.")
