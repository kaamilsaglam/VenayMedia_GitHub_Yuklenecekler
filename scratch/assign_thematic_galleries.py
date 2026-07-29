import codecs
import os
import re

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')

with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Define the custom 2-photo galleries for each portfolio item ID
galleries = {
    "1": "gallery:[`https://images.unsplash.com/photo-1519225421980-715cb0215aed?q=80&w=1000&auto=format`,`https://images.unsplash.com/photo-1511285560929-80b456fea0bc?q=80&w=1000&auto=format`]",
    "2": "gallery:[`https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?q=80&w=1000&auto=format`,`https://images.unsplash.com/photo-1520854221256-17451cc331bf?q=80&w=1000&auto=format`]",
    "3": "gallery:[`https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?q=80&w=1000&auto=format`,`https://images.unsplash.com/photo-1536240478700-b869070f9279?q=80&w=1000&auto=format`]",
    "4": "gallery:[`https://images.unsplash.com/photo-1542744173-8e7e53415bb0?q=80&w=1000&auto=format`,`https://images.unsplash.com/photo-1556761175-5973dc0f32e7?q=80&w=1000&auto=format`]",
    "5": "gallery:[`https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?q=80&w=1000&auto=format`,`https://images.unsplash.com/photo-1505330622279-bf7d7fc918f4?q=80&w=1000&auto=format`]",
    "6": "gallery:[`https://images.unsplash.com/photo-1554046920-90dcac471550?q=80&w=1000&auto=format`,`https://images.unsplash.com/photo-1516961642265-531546e84af2?q=80&w=1000&auto=format`]"
}

# Find all portfolio items and dynamically replace their gallery based on the ID.
# Format is like: {id:1,title:`...`,category:`...`,image:`...`,gallery:[...]}
def replace_gallery(match):
    full_str = match.group(0)
    item_id = match.group(1)
    # The gallery starts at match.group(2)
    # Reconstruct the string with the new gallery
    new_gallery = galleries.get(item_id)
    if new_gallery:
        # replace the gallery:[...] part with our new_gallery string
        return re.sub(r'gallery:\[[^\]]+\]', new_gallery, full_str)
    return full_str

js_content = re.sub(r'(\{id:(\d+),title:`[^`]+`,category:`[^`]+`,image:`[^`]+`,)gallery:\[[^\]]+\](\})', replace_gallery, js_content)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updates successful.")
