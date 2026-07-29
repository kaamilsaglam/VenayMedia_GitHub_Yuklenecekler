import codecs
import re

# 1. Update JS
js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace the text 'A' inside special-a span with the SVG
target_js = "(0,E.jsx)(`span`,{className:`special-a`,children:`A`})"
replacement_js = "(0,E.jsx)(`span`,{className:`special-a`,children:(0,E.jsx)(`svg`,{viewBox:`0 0 100 100`,preserveAspectRatio:`none`,children:(0,E.jsx)(`path`,{d:`M 45 0 Q -10 50 15 100 L 35 100 Q 30 50 45 0 Z M 45 0 L 65 0 L 95 100 L 75 100 Z`,fill:`currentColor`})})})"
js_content = js_content.replace(target_js, replacement_js)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

# 2. Update CSS
css_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-sFkQ3OzH.css'
with codecs.open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Remove old .special-a styles
css_content = re.sub(r'\.special-a\s*\{[^}]*\}', '', css_content)
css_content = re.sub(r'\.special-a::before\s*\{[^}]*\}', '', css_content)
css_content = re.sub(r'\.special-a::after\s*\{[^}]*\}', '', css_content)

# Append new .special-a styles
new_css = """
.special-a {
  position: relative !important;
  display: inline-block !important;
  width: 0.8em !important;
  height: 1em !important;
  margin: 0 0.02em !important;
}
.special-a svg {
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  width: 100% !important;
  height: 100% !important;
  fill: currentColor !important;
}
"""
css_content += new_css

with codecs.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated JS and CSS successfully!")
