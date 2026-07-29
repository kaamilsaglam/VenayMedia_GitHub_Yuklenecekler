import codecs

js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

perfect_svg = "(0,E.jsx)(`span`,{className:`special-a`,children:(0,E.jsx)(`svg`,{viewBox:`0 0 110 100`,preserveAspectRatio:`xMidYMid meet`,style:{overflow:`visible`},children:(0,E.jsx)(`path`,{d:`M 21.06 0 A 89.26 89.26 0 0 0 21.06 100 L 50 100 A 67.26 67.26 0 0 1 50 0 Z M 50 0 L 80 100 L 104 100 L 74 0 Z`,fill:`currentColor`})})})"

corrupted_svg = perfect_svg + "})"

if corrupted_svg in js_content:
    js_content = js_content.replace(corrupted_svg, perfect_svg)
    print("Fixed corrupted JS syntax!")
else:
    print("Corrupted SVG not found.")

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)
