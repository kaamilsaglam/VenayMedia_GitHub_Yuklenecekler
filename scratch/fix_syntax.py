import codecs

js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

perfect_svg = "(0,E.jsx)(`span`,{className:`special-a`,children:(0,E.jsx)(`svg`,{viewBox:`0 0 150 100`,preserveAspectRatio:`xMidYMid meet`,style:{overflow:`visible`},children:(0,E.jsx)(`path`,{d:`M 70 0 L 90 0 L 140 100 L 110 100 L 85 50 C 60 80, 40 100, 10 100 C 40 100, 30 40, 70 0 Z`,fill:`currentColor`})})})"

# Because my previous regex pattern `.*?\}\)\}\)` only matched TWO `})` 
# but perfect_svg contains THREE `})})})`, the replacement resulted in `perfect_svg + "})"`!
# Let's fix this by replacing the corrupted string with just `perfect_svg`.
corrupted_svg = perfect_svg + "})"

if corrupted_svg in js_content:
    js_content = js_content.replace(corrupted_svg, perfect_svg)
    print("Fixed corrupted JS syntax!")
else:
    print("Corrupted SVG not found. Checking if it's already fixed or something else.")

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)
