import os
import unicodedata

replacements = {
    "img/GPTs.png": "img/gpts_main.png",
    "img/Gpts2.png": "img/gpts_upload.png",
    "img/gpts3.png": "img/gpts_result.png",
    "img/2주차_스탭7.png": "img/antigravity_chat.png",
    "img/gift/md적용전.png": "img/gift/md_basic.png",
    "img/gift/md적용후(라이트).png": "img/gift/md_light.png",
    "img/gift/md적용후(다크).png": "img/gift/md_dark.png"
}

def normalize_nfc(s):
    return unicodedata.normalize('NFC', s)

def normalize_nfd(s):
    return unicodedata.normalize('NFD', s)

html_files = ["index.html", "light-coaching-v5.html"]

for html_file in html_files:
    if not os.path.exists(html_file):
        continue
        
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    updated = content
    for old, new in replacements.items():
        # Handle regular replacement
        updated = updated.replace(old, new)
        
        # Handle cases where path might contain NFC or NFD Korean letters
        old_nfc = normalize_nfc(old)
        old_nfd = normalize_nfd(old)
        
        updated = updated.replace(old_nfc, new)
        updated = updated.replace(old_nfd, new)
        
        # Also handle possible URL encoded versions
        import urllib.parse
        old_url_nfc = urllib.parse.quote(old_nfc)
        old_url_nfd = urllib.parse.quote(old_nfd)
        updated = updated.replace(old_url_nfc, new)
        updated = updated.replace(old_url_nfd, new)

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"Done updating: {html_file}")
