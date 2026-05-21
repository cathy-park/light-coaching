import os
import re
import unicodedata

# File path mapping based on semantic translation and ASCII conversion
mapping = {
    "안티그라피.png": "antigravity.png",
    "안티그라피.webp": "antigravity.webp",
    "안티그라피2.png": "antigravity2.png",
    "안티그라피3.png": "antigravity3.png",
    "안티그라피_다운로드.png": "antigravity_download.png",
    "폴더.png": "folder.png",
    "크롬.png": "chrome.png",
    "오리엔테이션_통계 뷰.png": "orientation_stats.png",
    "올라마화면.png": "ollama_screen.png",
    "오리엔테이션_캘린더뷰.png": "orientation_calendar.png",
    "오리엔테이션_업무입력_완료체크.png": "orientation_input_check.png",
    "올라마_다운.png": "ollama_download.png"
}

def normalize_nfc(s):
    return unicodedata.normalize('NFC', s)

def normalize_nfd(s):
    return unicodedata.normalize('NFD', s)

img_dir = "img"
print("Renaming files on disk...")
files_in_dir = os.listdir(img_dir)

# First rename on disk
for old_name, new_name in mapping.items():
    found = False
    # Match both NFC and NFD representations
    for file in files_in_dir:
        if normalize_nfc(file) == normalize_nfc(old_name) or normalize_nfd(file) == normalize_nfd(old_name):
            old_path = os.path.join(img_dir, file)
            new_path = os.path.join(img_dir, new_name)
            print(f"Renaming {old_path} -> {new_path}")
            os.rename(old_path, new_path)
            found = True
            break
    if not found:
        print(f"Warning: Could not find file for renaming: {old_name}")

# Now replace in HTML files
html_files = ["index.html", "light-coaching-v5.html"]

for html_file in html_files:
    if not os.path.exists(html_file):
        print(f"File {html_file} does not exist.")
        continue
    
    print(f"Updating references in {html_file}...")
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    updated_content = content
    for old_name, new_name in mapping.items():
        # Build pattern to handle both NFC and NFD encodings in the HTML content as well.
        # Some editors save as NFC, some browsers copy paste as NFD, etc.
        # Replace both forms.
        nfc_ver = normalize_nfc(old_name)
        nfd_ver = normalize_nfd(old_name)
        
        updated_content = updated_content.replace(nfc_ver, new_name)
        updated_content = updated_content.replace(nfd_ver, new_name)
        
        # Also handle urlencoded representations if any
        import urllib.parse
        encoded_nfc = urllib.parse.quote(nfc_ver)
        encoded_nfd = urllib.parse.quote(nfd_ver)
        updated_content = updated_content.replace(encoded_nfc, new_name)
        updated_content = updated_content.replace(encoded_nfd, new_name)

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print(f"Finished updating {html_file}.")
