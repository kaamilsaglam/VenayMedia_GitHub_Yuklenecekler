import codecs
import re

js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# The new ultra-wide, geometrically flawless SVG 
perfect_svg = "(0,E.jsx)(`span`,{className:`special-a`,children:(0,E.jsx)(`svg`,{viewBox:`0 0 150 100`,preserveAspectRatio:`xMidYMid meet`,style:{overflow:`visible`},children:(0,E.jsx)(`path`,{d:`M 70 0 L 90 0 L 140 100 L 110 100 L 85 50 C 60 80, 40 100, 10 100 C 40 100, 30 40, 70 0 Z`,fill:`currentColor`})})})"

pattern = r'\(0,E\.jsx\)\(`span`,\{className:`special-a`,children:\(0,E\.jsx\)\(`svg`,.*?\}\)\}\)'
matches = len(re.findall(pattern, js_content))
print(f"Found {matches} matches in JS.")

js_content = re.sub(pattern, perfect_svg, js_content)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)
print("Updated JS with WIDE FLAWLESS SVG successfully!")


css_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-sFkQ3OzH.css'
with codecs.open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# We need to update the width of .special-a to allow it to be wide.
# Let's replace width: 0.8em with width: 1.5em
css_content = re.sub(r'width:\s*0\.8em\s*!important;', 'width: 1.5em !important;', css_content)

with codecs.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)
print("Updated CSS width to 1.5em successfully!")

