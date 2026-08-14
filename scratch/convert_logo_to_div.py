import re
import glob
import os

js_files = glob.glob('assets/*.js')
if not js_files:
    print("No JS files found")
    exit(1)

js_file = js_files[0]
with open(js_file, 'r', encoding='utf-8') as f:
    data = f.read()

header_match = re.search(r'\(0,\w+\.\w+\)\(`img`,{[^}]+className:`header-logo-img`[^}]*}\)', data)
if header_match:
    print("Found header logo:", header_match.group(0))
    new_header = header_match.group(0).replace('`img`', '`div`')
    new_header = re.sub(r'src:`[^`]+`,', '', new_header)
    new_header = re.sub(r'alt:`[^`]+`,', '', new_header)
    data = data.replace(header_match.group(0), new_header)
else:
    print("Header logo not found with regex")

splash_match = re.search(r'\(0,\w+\.\w+\)\(`img`,{[^}]+className:`splash-logo-img`[^}]*}\)', data)
if splash_match:
    print("Found splash logo:", splash_match.group(0))
    new_splash = splash_match.group(0).replace('`img`', '`div`')
    new_splash = re.sub(r'src:`[^`]+`,', '', new_splash)
    new_splash = re.sub(r'alt:`[^`]+`,', '', new_splash)
    data = data.replace(splash_match.group(0), new_splash)
else:
    print("Splash logo not found with regex")

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(data)
print("Updated JS file")
