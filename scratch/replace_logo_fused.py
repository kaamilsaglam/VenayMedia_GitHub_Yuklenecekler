import codecs
import re

js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# The mathematically perfect Fused Glyph (Concentric Crescent + Lambda Right Leg)
perfect_svg = "(0,E.jsx)(`span`,{className:`special-a`,children:(0,E.jsx)(`svg`,{viewBox:`0 0 110 100`,preserveAspectRatio:`xMidYMid meet`,style:{overflow:`visible`},children:(0,E.jsx)(`path`,{d:`M 21.06 0 A 89.26 89.26 0 0 0 21.06 100 L 50 100 A 67.26 67.26 0 0 1 50 0 Z M 50 0 L 80 100 L 104 100 L 74 0 Z`,fill:`currentColor`})})})"

pattern = r'\(0,E\.jsx\)\(`span`,\{className:`special-a`,children:\(0,E\.jsx\)\(`svg`,.*?\}\)\}\)'
js_content = re.sub(pattern, perfect_svg, js_content)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)
print("Updated JS with FUSED CONCENTRIC SVG successfully!")

css_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-sFkQ3OzH.css'
with codecs.open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content = re.sub(r'width:\s*0\.7em\s*!important;', 'width: 1.0em !important;', css_content)

with codecs.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)
print("Updated CSS width to 1.0em successfully!")
