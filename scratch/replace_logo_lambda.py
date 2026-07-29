import codecs
import re

js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# The mathematically perfect Lambda A
perfect_svg = "(0,E.jsx)(`span`,{className:`special-a`,children:(0,E.jsx)(`svg`,{viewBox:`0 0 70 100`,preserveAspectRatio:`xMidYMid meet`,style:{overflow:`visible`},children:(0,E.jsx)(`path`,{d:`M 35 0 L 0 100 L 24.5 100 L 35 30 L 45.5 100 L 70 100 Z`,fill:`currentColor`})})})"

pattern = r'\(0,E\.jsx\)\(`span`,\{className:`special-a`,children:\(0,E\.jsx\)\(`svg`,.*?\}\)\}\)'
matches = len(re.findall(pattern, js_content))
print(f"Found {matches} matches in JS.")

js_content = re.sub(pattern, perfect_svg, js_content)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)
print("Updated JS with LAMBDA SVG successfully!")

css_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-sFkQ3OzH.css'
with codecs.open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content = re.sub(r'width:\s*1\.3em\s*!important;', 'width: 0.7em !important;', css_content)

with codecs.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)
print("Updated CSS width to 0.7em successfully!")
