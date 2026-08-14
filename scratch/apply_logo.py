import codecs

js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'

with codecs.open(js_path, 'r', 'utf-8', errors='ignore') as f:
    js = f.read()

target1 = "(0,E.jsxs)(`div`,{className:`logo-venay`,children:`VENAY`}),(0,E.jsx)(`div`,{className:`logo-media`,children:`M E D İ A`})"
replacement1 = "(0,E.jsx)(`img`,{src:`./logo.png`,alt:`Venay Media`,className:`splash-logo-img`,style:{height:`80px`,width:`auto`,objectFit:`contain`,margin:`0 auto`}})"

target2 = "(0,E.jsxs)(`span`,{className:`logo-venay`,children:`VENAY`}),(0,E.jsx)(`span`,{className:`logo-media`,children:`M E D İ A`})"
replacement2 = "(0,E.jsx)(`img`,{src:`./logo.png`,alt:`Venay Media`,className:`header-logo-img`,style:{height:`50px`,width:`auto`,objectFit:`contain`}})"

if target1 in js:
    js = js.replace(target1, replacement1)
    print("Replaced splash logo!")
else:
    print("Target 1 not found!")

if target2 in js:
    js = js.replace(target2, replacement2)
    print("Replaced header logo!")
else:
    print("Target 2 not found!")

with codecs.open(js_path, 'w', 'utf-8') as f:
    f.write(js)
    print("Saved js file.")
