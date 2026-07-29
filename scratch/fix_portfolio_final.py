import codecs
import os
import re

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')

with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Make sure the old URLs are EXACTLY what they were initially
js_content = js_content.replace("https://images.unsplash.com/photo-1492691527719-9d1e07e534b4", "https://images.unsplash.com/photo-1601506521937-0121a7fc2a6b")
js_content = js_content.replace("https://images.unsplash.com/photo-1554046920-90dcac471550", "https://images.unsplash.com/photo-1516035069371-29a1b244cc32")

# Let's hide the texts under the photos in portfolio.
# The user said "sadece orada fotoğrafların altında bulunan yazıları kaldır".
# We can inject a CSS rule into index.html to hide .portfolio-info
html_path = os.path.join(base_dir, 'index.html')
with codecs.open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

hide_css = "<style>.portfolio-info { display: none !important; }</style>"
if hide_css not in html_content:
    html_content = html_content.replace("</head>", hide_css + "\n</head>")

with codecs.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# To make all gallery arrays have the exact same size, we need to regex replace all `gallery:[...]` with a fixed array of 4 images.
# Let's use 4 reliable, varied Unsplash images that were already used in the galleries.
fixed_gallery = "gallery:[`https://images.unsplash.com/photo-1519225421980-715cb0215aed?q=80&w=1000&auto=format`,`https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?q=80&w=1000&auto=format`,`https://images.unsplash.com/photo-1601506521937-0121a7fc2a6b?q=80&w=1000&auto=format`,`https://images.unsplash.com/photo-1542744173-8e7e53415bb0?q=80&w=1000&auto=format`]"

# Replace all gallery arrays in the portfolio objects
js_content = re.sub(r'gallery:\[[^\]]+\]', fixed_gallery, js_content)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updates successful.")
