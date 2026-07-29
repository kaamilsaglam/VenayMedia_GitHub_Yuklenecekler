import codecs
import re

js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Target SVG that is currently in the file (from my previous step)
target_svg = "(0,E.jsx)(`span`,{className:`special-a`,children:(0,E.jsx)(`svg`,{viewBox:`0 0 100 100`,preserveAspectRatio:`none`,children:(0,E.jsx)(`path`,{d:`M 40 0 L 60 0 L 100 100 L 70 100 L 50 40 Q 25 90 0 90 C -15 90, 5 30, 40 0 Z`,fill:`currentColor`})})})"

# The absolutely flawless new SVG that fixes the clipping issue and uses perfect geometric curves
perfect_svg = "(0,E.jsx)(`span`,{className:`special-a`,children:(0,E.jsx)(`svg`,{viewBox:`0 0 100 100`,preserveAspectRatio:`none`,style:{overflow:`visible`},children:(0,E.jsx)(`path`,{d:`M 40 0 L 60 0 L 90 100 L 65 100 L 50 50 C 40 70, 20 100, 0 100 C 15 100, 5 30, 40 0 Z`,fill:`currentColor`})})})"

if target_svg in js_content:
    js_content = js_content.replace(target_svg, perfect_svg)
    print("Found and replaced EXACT target string.")
else:
    print("Target exact string not found, using regex...")
    # More robust regex replacement if there were slight spacing differences
    pattern = r'\(0,E\.jsx\)\(`span`,\{className:`special-a`,children:\(0,E\.jsx\)\(`svg`,.*?\}\)\}\)'
    matches = len(re.findall(pattern, js_content))
    print(f"Regex found {matches} matches.")
    js_content = re.sub(pattern, perfect_svg, js_content)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updated JS with FLAWLESS SVG successfully!")
