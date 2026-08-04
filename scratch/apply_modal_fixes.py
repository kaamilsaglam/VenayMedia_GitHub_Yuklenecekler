import codecs
import re

print("Starting modal optimizations...")

css_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-sFkQ3OzH.css'
with codecs.open(css_path, 'r', 'utf-8', errors='ignore') as f:
    css = f.read()

modal_css = """
/* Modal Optimizations */
.modal-overlay {
  will-change: opacity, backdrop-filter;
  transform: translateZ(0);
}
.modal-content {
  overscroll-behavior: contain;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: thin; /* Firefox */
  scrollbar-color: var(--color-accent-gold) transparent;
}
/* Chrome, Safari, Edge custom scrollbar for modal */
.modal-content::-webkit-scrollbar {
  width: 6px;
}
.modal-content::-webkit-scrollbar-track {
  background: transparent;
}
.modal-content::-webkit-scrollbar-thumb {
  background-color: var(--color-accent-gold);
  border-radius: 10px;
}
"""

if "overscroll-behavior: contain" not in css:
    css += modal_css

with codecs.open(css_path, 'w', 'utf-8') as f:
    f.write(css)
print("CSS updated.")

html_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\index.html'
with codecs.open(html_path, 'r', 'utf-8', errors='ignore') as f:
    html = f.read()

html = re.sub(r'v=\d+', 'v=11', html)

with codecs.open(html_path, 'w', 'utf-8') as f:
    f.write(html)
print("HTML cache bumped to v11.")
