import os
import shutil
import codecs

src_dir = r"C:\Users\Kamil\.gemini\antigravity-ide\brain\4beec34c-4047-47ef-b24e-0a01e35e88f8"
dest_dir = r"c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\ig_posts"

os.makedirs(dest_dir, exist_ok=True)

images = [
    "media__1785362275639.png",
    "media__1785362275716.jpg",
    "media__1785362275810.jpg",
    "media__1785362275818.jpg"
]

for idx, img in enumerate(images):
    ext = img.split('.')[-1]
    shutil.copy(os.path.join(src_dir, img), os.path.join(dest_dir, f"post_{idx}.{ext}"))

js_path = r"c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js"
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace `fe.map` with new array
js_content = js_content.replace(
    'className:`instagram-grid`,children:fe.map((e,t)=>(0,E.jsxs)',
    'className:`instagram-grid`,children:["./assets/ig_posts/post_0.png", "./assets/ig_posts/post_1.jpg", "./assets/ig_posts/post_2.jpg", "./assets/ig_posts/post_3.jpg"].map((e,t)=>(0,E.jsxs)'
)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

html_path = r"c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\index.html"
with codecs.open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Modify the script in index.html to output "Takip Et" instead of original text
html_content = html_content.replace(
    "btn.innerHTML = igSvg + btn.textContent;",
    "btn.innerHTML = igSvg + 'Takip Et';"
)
# Also handle the edge case if the text doesn't match perfectly.
html_content = html_content.replace(
    "if(btn.textContent.includes('Takip Edin') && !btn.innerHTML.includes('svg')) {",
    "if(btn.textContent.includes('Takip Edin') && !btn.innerHTML.includes('svg')) {\n            btn.textContent = 'Takip Et';"
)

with codecs.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updates completed successfully.")
