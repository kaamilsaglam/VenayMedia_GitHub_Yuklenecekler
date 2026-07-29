import urllib.request
import os
import codecs
import re

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
img_dir = os.path.join(base_dir, 'assets', 'ig_posts')

# Ensure directory exists
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

# Mapping of concept ID to 2 image URLs that we will download
# We use source.unsplash.com or standard image URLs that we can download using a User-Agent.
image_sources = {
    "1": [
        "https://images.unsplash.com/photo-1519225421980-715cb0215aed?q=80&w=800&auto=format",
        "https://images.unsplash.com/photo-1511285560929-80b456fea0bc?q=80&w=800&auto=format"
    ],
    "2": [
        "https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?q=80&w=800&auto=format",
        "https://images.unsplash.com/photo-1520854221256-17451cc331bf?q=80&w=800&auto=format"
    ],
    "3": [
        "https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?q=80&w=800&auto=format",
        "https://images.unsplash.com/photo-1536240478700-b869070f9279?q=80&w=800&auto=format"
    ],
    "4": [
        "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?q=80&w=800&auto=format",
        "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?q=80&w=800&auto=format"
    ],
    "5": [
        "https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?q=80&w=800&auto=format",
        "https://images.unsplash.com/photo-1505330622279-bf7d7fc918f4?q=80&w=800&auto=format"
    ],
    "6": [
        "https://images.unsplash.com/photo-1554046920-90dcac471550?q=80&w=800&auto=format",
        "https://images.unsplash.com/photo-1516961642265-531546e84af2?q=80&w=800&auto=format"
    ]
}

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')]
urllib.request.install_opener(opener)

galleries_local = {}

for pid, urls in image_sources.items():
    local_paths = []
    for i, url in enumerate(urls):
        filename = f"port_{pid}_{i+1}.jpg"
        filepath = os.path.join(img_dir, filename)
        try:
            urllib.request.urlretrieve(url, filepath)
            local_paths.append(f"`./assets/ig_posts/{filename}`")
            print(f"Downloaded {filename}")
        except Exception as e:
            print(f"Failed to download {filename}: {e}")
            # fallback to a known local image if download fails
            local_paths.append(f"`./assets/ig_posts/post_{i+1}.jpg`")
    
    galleries_local[pid] = f"gallery:[{','.join(local_paths)}]"

js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

def replace_gallery(match):
    full_str = match.group(0)
    item_id = match.group(1)
    new_gallery = galleries_local.get(item_id)
    if new_gallery:
        return re.sub(r'gallery:\[[^\]]+\]', new_gallery, full_str)
    return full_str

js_content = re.sub(r'(\{id:(\d+),title:`[^`]+`,category:`[^`]+`,image:`[^`]+`,)gallery:\[[^\]]+\](\})', replace_gallery, js_content)

# Also update the MAIN image for each portfolio item to be the first of its gallery
def replace_main_image(match):
    full_str = match.group(0)
    item_id = match.group(1)
    # The first image is port_{item_id}_1.jpg
    new_img = f"image:`./assets/ig_posts/port_{item_id}_1.jpg`"
    return re.sub(r'image:`[^`]+`', new_img, full_str)

js_content = re.sub(r'(\{id:(\d+),title:`[^`]+`,category:`[^`]+`,)image:`[^`]+`', replace_main_image, js_content)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updates successful.")
