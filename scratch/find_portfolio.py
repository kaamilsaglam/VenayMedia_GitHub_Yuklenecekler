import codecs
import os
import re

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')

with codecs.open(js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find portfolio items: {id:1,title:`...`,category:`...`,image:`...`}
matches = re.finditer(r'\{id:\d+,title:`[^`]+`,category:`[^`]+`,image:`[^`]+`', content)
for m in matches:
    print(m.group(0))
