import codecs
import re

print("Starting full re-application of all changes...")

# 1. Fix JS File
js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Fix Konum
js_content = js_content.replace('Konum: Konya, Selçuklu', 'Konya, Selçuklu')

# Fix Fikirlerin Karanlıktaki Işığı (remove <br>)
target2 = "children:[`Fikirlerin`,(0,E.jsx)(`br`,{}),`Karanlıktaki Işığı`]"
replacement2 = "children:[`Fikirlerin Karanlıktaki Işığı`]"
js_content = js_content.replace(target2, replacement2)

# Ensure the 5-item array with insta0.png and centered logo (insta1.png is 3rd)
old_fe_4 = "fe=[`./assets/insta1.png`,`./assets/insta2.png`,`./assets/insta3.png`,`./assets/insta4.png`]"
old_fe_5_bad = "fe=[`./assets/intsa0.png`,`./assets/insta2.png`,`./assets/insta1.png`,`./assets/insta3.png`,`./assets/insta4.png`]"
correct_fe = "fe=[`./assets/insta0.png`,`./assets/insta2.png`,`./assets/insta1.png`,`./assets/insta3.png`,`./assets/insta4.png`]"
js_content = js_content.replace(old_fe_4, correct_fe)
js_content = js_content.replace(old_fe_5_bad, correct_fe)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)
print("JS fixes applied.")

# 2. Fix CSS File
css_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-sFkQ3OzH.css'
with codecs.open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content = css_content.replace(".instagram-grid{grid-template-columns:repeat(4,1fr)", ".instagram-grid{grid-template-columns:repeat(5,1fr)")

mobile_css = "@media (max-width: 992px) { .instagram-grid .ig-post:nth-child(3) { grid-column: 1 / -1; width: 50%; margin: 0 auto; } }"
if mobile_css not in css_content:
    css_content += "\n" + mobile_css

with codecs.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)
print("CSS fixes applied.")

# 3. Fix HTML Cache buster
html_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\index.html'
with codecs.open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = re.sub(r'index-3nv5kxFG\.js\?v=\d+', 'index-3nv5kxFG.js?v=4', html_content)
html_content = re.sub(r'index-3nv5kxFG\.js"', 'index-3nv5kxFG.js?v=4"', html_content)
html_content = re.sub(r'index-sFkQ3OzH\.css\?v=\d+', 'index-sFkQ3OzH.css?v=4', html_content)
html_content = re.sub(r'index-sFkQ3OzH\.css"', 'index-sFkQ3OzH.css?v=4"', html_content)

with codecs.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print("HTML cache bust (v=4) applied.")

print("All modifications successfully applied.")
