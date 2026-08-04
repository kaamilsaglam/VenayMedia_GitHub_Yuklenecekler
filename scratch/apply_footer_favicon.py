import codecs
import re

print("Starting footer and favicon updates...")

# 1. Update HTML Favicon
html_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\index.html'
with codecs.open(html_path, 'r', 'utf-8', errors='ignore') as f:
    html = f.read()

# Replace favicon
html = html.replace('href="/vite.svg"', 'href="./favicon.svg"')

# Bump cache to v13
html = re.sub(r'v=\d+', 'v=13', html)

with codecs.open(html_path, 'w', 'utf-8') as f:
    f.write(html)
print("HTML updated.")


# 2. Update Footer in JS
js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(js_path, 'r', 'utf-8', errors='ignore') as f:
    js = f.read()

old_footer = "Venay Media. Tüm hakları saklıdır."
# Using Unicode escaped strings in case of file encoding wonkiness, but utf-8 is fine.
new_footer = "Venay Media. Tüm hakları saklıdır. | Dijital Mimari & Tasarım: Hacı Kamil Sağlam"

if old_footer in js:
    js = js.replace(old_footer, new_footer)
else:
    print("Warning: Old footer not found exactly as string. Checking with escaped characters...")
    # Sometimes it might be encoded as T\u00fcm haklar\u0131 sakl\u0131d\u0131r.
    old_encoded = "Venay Media. T\xc3\xbcm haklar\xc4\xb1 sakl\xc4\xb1d\xc4\xb1r."
    if old_encoded in js:
        js = js.replace(old_encoded, new_footer)

with codecs.open(js_path, 'w', 'utf-8') as f:
    f.write(js)
print("JS updated.")
