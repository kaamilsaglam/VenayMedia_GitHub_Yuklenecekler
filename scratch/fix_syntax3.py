import codecs

js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

perfect_svg = "(0,E.jsx)(`span`,{className:`special-a`,children:(0,E.jsx)(`svg`,{viewBox:`0 0 70 100`,preserveAspectRatio:`xMidYMid meet`,style:{overflow:`visible`},children:(0,E.jsx)(`path`,{d:`M 35 0 L 0 100 L 24.5 100 L 35 30 L 45.5 100 L 70 100 Z`,fill:`currentColor`})})})"

corrupted_svg = perfect_svg + "})"

if corrupted_svg in js_content:
    js_content = js_content.replace(corrupted_svg, perfect_svg)
    print("Fixed corrupted JS syntax!")
else:
    print("Corrupted SVG not found.")

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)
