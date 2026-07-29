import codecs
import os
import re

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')

with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Revert the image URLs
old_url_1 = "./assets/ig_posts/post_new.jpg"
new_url_1 = "https://images.unsplash.com/photo-1601506521937-0121a7fc2a6b?q=80&w=1000&auto=format"
js_content = js_content.replace(old_url_1, new_url_1)

old_url_2 = "./assets/ig_posts/post_third.jpg"
new_url_2 = "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?q=80&w=1000&auto=format"
js_content = js_content.replace(old_url_2, new_url_2)

# Fix the broken Unsplash URLs by pointing them to a similar, working Unsplash image or remove the query parameters!
# Unsplash sometimes breaks if query params are old.
js_content = js_content.replace("https://images.unsplash.com/photo-1601506521937-0121a7fc2a6b?q=80&w=1000&auto=format", "https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?q=80&w=1000&auto=format")
js_content = js_content.replace("https://images.unsplash.com/photo-1516035069371-29a1b244cc32?q=80&w=1000&auto=format", "https://images.unsplash.com/photo-1554046920-90dcac471550?q=80&w=1000&auto=format")

# Let's extract the portfolio array and look at the gallery arrays.
matches = re.finditer(r'\{id:\d+,title:`[^`]+`,category:`[^`]+`,image:`[^`]+`,gallery:\[([^\]]+)\]\}', js_content)
for m in matches:
    print(m.group(0))

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

