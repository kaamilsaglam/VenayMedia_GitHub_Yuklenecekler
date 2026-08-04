import codecs
import re

# Update JS file
js_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Current array: fe=[`./assets/insta1.png`,`./assets/insta2.png`,`./assets/insta3.png`,`./assets/insta4.png`]
# Change to: fe=[`./assets/insta0.png`,`./assets/insta2.png`,`./assets/insta1.png`,`./assets/insta3.png`,`./assets/insta4.png`]
old_array = "fe=[`./assets/insta1.png`,`./assets/insta2.png`,`./assets/insta3.png`,`./assets/insta4.png`]"
new_array = "fe=[`./assets/insta0.png`,`./assets/insta2.png`,`./assets/insta1.png`,`./assets/insta3.png`,`./assets/insta4.png`]"

if old_array in js_content:
    js_content = js_content.replace(old_array, new_array)
else:
    # Just in case there are single quotes or something
    old_array_2 = "fe=['./assets/insta1.png','./assets/insta2.png','./assets/insta3.png','./assets/insta4.png']"
    if old_array_2 in js_content:
        js_content = js_content.replace(old_array_2, new_array)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

# Update CSS file
css_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-sFkQ3OzH.css'
with codecs.open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Change desktop grid to 5 columns
css_content = css_content.replace(".instagram-grid{grid-template-columns:repeat(4,1fr)", ".instagram-grid{grid-template-columns:repeat(5,1fr)")

# Add media query for the center logo on mobile/tablet
# I'll inject it right after the .instagram-grid definition
if ".ig-post:nth-child(3)" not in css_content:
    injection = "@media (max-width: 992px) { .instagram-grid .ig-post:nth-child(3) { grid-column: 1 / -1; width: 50%; margin: 0 auto; } } "
    css_content = css_content + injection

with codecs.open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Modifications applied.")
