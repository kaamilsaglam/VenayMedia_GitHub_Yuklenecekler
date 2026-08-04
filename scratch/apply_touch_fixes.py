import codecs
import re

print("Starting mobile touch optimizations...")

css_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-sFkQ3OzH.css'
with codecs.open(css_path, 'r', 'utf-8', errors='ignore') as f:
    css = f.read()

touch_css = """
/* Prevent copy mode & selection globally */
html, body {
  background-color: var(--color-bg, #111) !important;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
/* Ensure form elements remain selectable/usable */
input, textarea, select {
  -webkit-user-select: auto;
  user-select: auto;
}
/* Remove 300ms tap delay & ensure zero black flash */
a, button, .ig-post, .portfolio-item, .btn {
  touch-action: manipulation;
  -webkit-tap-highlight-color: rgba(0,0,0,0) !important;
  background-color: transparent;
}
/* Remove any outline on click */
a:focus, button:focus {
  outline: none;
}
"""

if "touch-action: manipulation" not in css:
    css += touch_css

with codecs.open(css_path, 'w', 'utf-8') as f:
    f.write(css)
print("CSS updated.")

html_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\index.html'
with codecs.open(html_path, 'r', 'utf-8', errors='ignore') as f:
    html = f.read()

html = re.sub(r'v=\d+', 'v=10', html)

with codecs.open(html_path, 'w', 'utf-8') as f:
    f.write(html)
print("HTML cache bumped to v10.")
