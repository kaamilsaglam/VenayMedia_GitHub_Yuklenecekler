import codecs
import re

js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# The mathematically perfect right-facing crescent formed by two intersecting circles
perfect_svg = "(0,E.jsx)(`span`,{className:`special-a`,children:(0,E.jsx)(`svg`,{viewBox:`0 0 130 100`,preserveAspectRatio:`xMidYMid meet`,style:{overflow:`visible`},children:(0,E.jsx)(`path`,{d:`M 60 0 A 60 60 0 0 1 25 100 A 150 150 0 0 0 60 0 Z M 60 0 L 85 0 L 120 100 L 95 100 Z`,fill:`currentColor`})})})"

pattern = r'\(0,E\.jsx\)\(`span`,\{className:`special-a`,children:\(0,E\.jsx\)\(`svg`,.*?\}\)\}\)'
matches = len(re.findall(pattern, js_content))
print(f"Found {matches} matches in JS.")

js_content = re.sub(pattern, perfect_svg, js_content)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)
print("Updated JS with GEOMETRIC CIRCLE SVG successfully!")

css_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-sFkQ3OzH.css'
with codecs.open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content = re.sub(r'width:\s*1\.5em\s*!important;', 'width: 1.3em !important;', css_content)

with codecs.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)
print("Updated CSS width to 1.3em successfully!")
