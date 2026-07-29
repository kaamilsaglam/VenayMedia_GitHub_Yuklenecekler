import codecs
import os
import re

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')

with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Fix the broken image paths
def fix_broken_image(match):
    # match.group(1) is the item ID
    item_id = match.group(1)
    return f"image:`./assets/ig_posts/port_{item_id}_1.jpg`"

js_content = re.sub(r'image:`\./assets/ig_posts/port_\{id:(\d+),title:`[^`]+`,category:`[^`]+`,_1\.jpg`', fix_broken_image, js_content)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updates successful.")
