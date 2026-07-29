import codecs
import re

# Update JS with the perfected SVG path
js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# We need to replace the previous SVG with the new one.
# First, let's locate the span.special-a and its contents.
# Since we already replaced it in the last step, we can search for the SVG block.
# The previous replacement was:
# (0,E.jsx)(`span`,{className:`special-a`,children:(0,E.jsx)(`svg`,{viewBox:`0 0 100 100`,preserveAspectRatio:`none`,children:(0,E.jsx)(`path`,{d:`M 45 0 Q -10 50 15 100 L 35 100 Q 30 50 45 0 Z M 45 0 L 65 0 L 95 100 L 75 100 Z`,fill:`currentColor`})})})

target_svg = "(0,E.jsx)(`span`,{className:`special-a`,children:(0,E.jsx)(`svg`,{viewBox:`0 0 100 100`,preserveAspectRatio:`none`,children:(0,E.jsx)(`path`,{d:`M 45 0 Q -10 50 15 100 L 35 100 Q 30 50 45 0 Z M 45 0 L 65 0 L 95 100 L 75 100 Z`,fill:`currentColor`})})})"
perfect_svg = "(0,E.jsx)(`span`,{className:`special-a`,children:(0,E.jsx)(`svg`,{viewBox:`0 0 100 100`,preserveAspectRatio:`none`,children:(0,E.jsx)(`path`,{d:`M 40 0 L 60 0 L 100 100 L 70 100 L 50 40 Q 25 90 0 90 C -15 90, 5 30, 40 0 Z`,fill:`currentColor`})})})"

if target_svg in js_content:
    js_content = js_content.replace(target_svg, perfect_svg)
else:
    print("Warning: Target SVG not found exactly. Using regex.")
    js_content = re.sub(r'\(0,E\.jsx\)\(`span`,\{className:`special-a`,children:\(0,E\.jsx\)\(`svg`,.*?\}\)\}\)', perfect_svg, js_content)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updated JS with PERFECT SVG successfully!")
