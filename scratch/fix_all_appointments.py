import codecs
import os

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
html_path = os.path.join(base_dir, 'index.html')

with codecs.open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

import re

# Find the block where we attach the whatsapp modal
old_block = """document.querySelectorAll('.btn, .btn-primary, .wa-button, a, button').forEach(function(btn) {
          if ((btn.textContent && btn.textContent.includes('Randevu Al')) || btn.classList.contains('wa-button')) {"""

new_block = """document.querySelectorAll('.btn, .btn-primary, .wa-button, a, button').forEach(function(btn) {
          var text = (btn.textContent || '').toUpperCase();
          if (text.includes('RANDEVU') || btn.classList.contains('wa-button')) {"""

if old_block in html_content:
    html_content = html_content.replace(old_block, new_block)
else:
    print("Warning: old block not found. Trying regex.")
    html_content = re.sub(r'document\.querySelectorAll\(\'\.btn.*?\{[^}]*?includes\(\'Randevu Al\'\).*?\{', new_block, html_content, flags=re.DOTALL)

with codecs.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updates successful.")
