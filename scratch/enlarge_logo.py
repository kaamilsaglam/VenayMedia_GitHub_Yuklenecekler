import codecs

js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'

with codecs.open(js_path, 'r', 'utf-8', errors='ignore') as f:
    js = f.read()

old_splash = "(0,E.jsx)(`img`,{src:`./logo.png`,alt:`Venay Media`,className:`splash-logo-img`,style:{height:`120px`,maxWidth:`90vw`,width:`auto`,objectFit:`contain`,margin:`0 auto`}})"
new_splash = "(0,E.jsx)(`img`,{src:`./logo.png`,alt:`Venay Media`,className:`splash-logo-img`,style:{height:`220px`,maxWidth:`90vw`,width:`auto`,objectFit:`contain`,margin:`0 auto`}})"

old_header = "(0,E.jsx)(`img`,{src:`./logo.png`,alt:`Venay Media`,className:`header-logo-img`,style:{height:`42px`,maxWidth:`100%`,width:`auto`,objectFit:`contain`}})"
new_header = "(0,E.jsx)(`img`,{src:`./logo.png`,alt:`Venay Media`,className:`header-logo-img`,style:{height:`75px`,maxWidth:`100%`,width:`auto`,objectFit:`contain`}})"

if old_splash in js:
    js = js.replace(old_splash, new_splash)
    print("Replaced splash logo size!")
else:
    print("Target splash not found!")

if old_header in js:
    js = js.replace(old_header, new_header)
    print("Replaced header logo size!")
else:
    print("Target header not found!")

with codecs.open(js_path, 'w', 'utf-8') as f:
    f.write(js)
    print("Saved js file.")
