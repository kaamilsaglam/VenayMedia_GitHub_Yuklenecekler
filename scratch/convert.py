import glob

js_file = glob.glob('assets/*.js')[0]
with open(js_file, 'r', encoding='utf-8') as f:
    data = f.read()

old_header = "(0,E.jsx)(`img`,{src:`./logo.png`,alt:`Venay Media`,className:`header-logo-img`,style:{height:`75px`,maxWidth:`100%`,width:`auto`,objectFit:`contain`}})"
new_header = "(0,E.jsx)(`div`,{className:`header-logo-img`,style:{height:`75px`,maxWidth:`100%`,width:`auto`,objectFit:`contain`}})"

old_splash = "(0,E.jsx)(`img`,{src:`./logo.png`,alt:`Venay Media`,className:`splash-logo-img`,style:{height:`220px`,maxWidth:`90vw`,width:`auto`,objectFit:`contain`,margin:`0 auto`}})"
new_splash = "(0,E.jsx)(`div`,{className:`splash-logo-img`,style:{height:`220px`,maxWidth:`90vw`,width:`auto`,objectFit:`contain`,margin:`0 auto`}})"

data = data.replace(old_header, new_header)
data = data.replace(old_splash, new_splash)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(data)

print("Replaced successfully")
