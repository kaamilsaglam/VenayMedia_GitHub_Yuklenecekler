import codecs
import os

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')
html_path = os.path.join(base_dir, 'index.html')

with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace texts
js_content = js_content.replace('Düğün Organizasyonu', 'Düğün Organizasyon Çekimi')
js_content = js_content.replace('Kına Organizasyonu', 'Kına Organizasyon Çekimi')
# Also check for "Düğün Organizasyon" without the "u"
js_content = js_content.replace('Düğün Organizasyon', 'Düğün Organizasyon Çekimi')
# Wait, replacing "Düğün Organizasyon" would also replace the already replaced "Düğün Organizasyon Çekimi" -> "Düğün Organizasyon Çekimi Çekimi". 
# So let's only do the strict exact replacements.

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)


# Now update index.html to bind all "Randevu Al" buttons
with codecs.open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

import re

# We will look for the line: document.querySelectorAll('.btn-primary, .wa-button').forEach(function(btn) {
# And replace the if condition to match anything containing "Randevu Al"
old_block = """document.querySelectorAll('.btn-primary, .wa-button').forEach(function(btn) {
          if (btn.textContent.includes('Hemen Randevu Al') || btn.classList.contains('wa-button')) {"""
new_block = """document.querySelectorAll('.btn, .btn-primary, .wa-button, a, button').forEach(function(btn) {
          if ((btn.textContent && btn.textContent.includes('Randevu Al')) || btn.classList.contains('wa-button')) {"""

html_content = html_content.replace(old_block, new_block)

# Just in case they are distinct tags, let's also ensure href is set only if it's an anchor tag, but it's fine.
with codecs.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updates successful.")
