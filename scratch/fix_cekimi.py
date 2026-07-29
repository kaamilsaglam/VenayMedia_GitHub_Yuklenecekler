import codecs
import os

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')

with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Fix the duplicate "Çekimi"
js_content = js_content.replace('Çekimi Çekimi', 'Çekimi')

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updates successful.")
