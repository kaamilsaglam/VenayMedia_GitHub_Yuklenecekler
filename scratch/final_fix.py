import codecs
import os
import re
import shutil

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')

# 1. Copy the new image for the Instagram section
source_img = r'C:\Users\Kamil\.gemini\antigravity-ide\brain\4beec34c-4047-47ef-b24e-0a01e35e88f8\media__1785365757773.jpg'
dest_img = os.path.join(base_dir, 'assets', 'ig_posts', 'post_new_4.jpg')
shutil.copyfile(source_img, dest_img)

with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# 2. Fix the Instagram Grid 4th image
correct_ig_grid = '["./assets/ig_posts/post_new.jpg", "./assets/ig_posts/post_0.png", "./assets/ig_posts/post_2.jpg", "./assets/ig_posts/post_new_4.jpg"]'
js_content = re.sub(r'className:`instagram-grid`,children:\[.*?\]', f'className:`instagram-grid`,children:{correct_ig_grid}', js_content)

# 3. Fix the Concept (Portfolio) Galleries
def replace_gallery(match):
    prefix = match.group(1) # {id:1,title:`...`,category:`...`,image:`...`,
    item_id = match.group(2) # 1
    suffix = match.group(3) # ,description:`...`
    
    # We set exactly 2 images for the gallery
    new_gallery = f"gallery:[`./assets/ig_posts/port_{item_id}_1.jpg`,`./assets/ig_posts/port_{item_id}_2.jpg`]"
    
    return f"{prefix}{new_gallery}{suffix}"

# Match `{id:X,...,image:...,gallery:[...],description:...}`
# Note we match everything up to `gallery:[...]` then capture `,description` onwards if needed.
js_content = re.sub(r'(\{id:(\d+),title:`[^`]+`,category:`[^`]+`,image:`[^`]+`,)gallery:\[[^\]]+\](,[^}]+})', replace_gallery, js_content)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updates successful.")
