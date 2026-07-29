import codecs
import os
import shutil

src_img = r"C:\Users\Kamil\.gemini\antigravity-ide\brain\4beec34c-4047-47ef-b24e-0a01e35e88f8\media__1785363195277.jpg"
dest_img = r"c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\ig_posts\post_third.jpg"

if os.path.exists(src_img):
    shutil.copy(src_img, dest_img)

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')

with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace the 3rd image in the array
js_content = js_content.replace(
    '["./assets/ig_posts/post_new.jpg", "./assets/ig_posts/post_0.png", "./assets/ig_posts/post_1.jpg", "./assets/ig_posts/post_2.jpg"]',
    '["./assets/ig_posts/post_new.jpg", "./assets/ig_posts/post_0.png", "./assets/ig_posts/post_third.jpg", "./assets/ig_posts/post_2.jpg"]'
)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updates successful.")
