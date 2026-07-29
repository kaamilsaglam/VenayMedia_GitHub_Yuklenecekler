import codecs
import os
import shutil

src_img = r"C:\Users\Kamil\.gemini\antigravity-ide\brain\4beec34c-4047-47ef-b24e-0a01e35e88f8\media__1785362602210.jpg"
dest_img = r"c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\ig_posts\post_new.jpg"

if os.path.exists(src_img):
    shutil.copy(src_img, dest_img)

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')
html_path = os.path.join(base_dir, 'index.html')

with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# 1. Update the images array
old_array = '["./assets/ig_posts/post_0.png", "./assets/ig_posts/post_1.jpg", "./assets/ig_posts/post_2.jpg", "./assets/ig_posts/post_3.jpg"]'
new_array = '["./assets/ig_posts/post_new.jpg", "./assets/ig_posts/post_0.png", "./assets/ig_posts/post_1.jpg", "./assets/ig_posts/post_2.jpg", "./assets/ig_posts/post_3.jpg"]'
js_content = js_content.replace(old_array, new_array)

# 2. Update address text
js_content = js_content.replace('Merkez Ofis, Konya', 'Konum: Konya, Selçuklu')

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)


# 3. Update index.html script to replace "IG" in overlays and properly handle the IG text in buttons
with codecs.open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Add logic for .ig-overlay div
new_script = """
        // Update IG overlays
        document.querySelectorAll('.ig-overlay div').forEach(function(div) {
          if (div.textContent === 'IG') {
            div.innerHTML = igSvg.replace('width="22" height="22"', 'width="32" height="32"').replace('margin-right:8px', 'margin-right:0');
          }
        });
"""

if '.ig-overlay div' not in html_content:
    html_content = html_content.replace('// Update Bizi Takip Edin button', new_script + '\n        // Update Bizi Takip Edin button')

with codecs.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updates successful.")
