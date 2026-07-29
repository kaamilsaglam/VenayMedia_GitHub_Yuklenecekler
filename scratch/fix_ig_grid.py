import codecs
import os
import re

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')

with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Fix the Instagram Grid that got broken by global URL replacements
# The user wants exactly: post_new.jpg first, then the remaining 3 original images.
# The original images before I broke it were: post_0.png, post_2.jpg, post_1.jpg (after removing post_third.jpg).
correct_ig_grid = '["./assets/ig_posts/post_new.jpg", "./assets/ig_posts/post_0.png", "./assets/ig_posts/post_2.jpg", "./assets/ig_posts/post_1.jpg"]'

# We find the instagram-grid className and the array right after it.
# It looks like: className:`instagram-grid`,children:["https://...", ...]
# So we can regex match it safely.
js_content = re.sub(r'className:`instagram-grid`,children:\[.*?\]', f'className:`instagram-grid`,children:{correct_ig_grid}', js_content)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updates successful.")
