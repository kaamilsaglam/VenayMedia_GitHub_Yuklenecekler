import codecs
import os

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')

with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace 1: Header Randevu Al button
old_1 = "onClick:g,style:{color:`var(--color-accent-gold)`},children:`Randevu Al`"
new_1 = "onClick:(e)=>{e.preventDefault();document.getElementById('whatsapp-modal').classList.add('open')},style:{color:`var(--color-accent-gold)`},children:`Randevu Al`"
js_content = js_content.replace(old_1, new_1)

# Replace 2: Portfolio Concept Randevu Al button
old_2 = "onClick:()=>g(null,u.category),children:`Bu Konsept"
new_2 = "onClick:(e)=>{e.preventDefault();document.getElementById('whatsapp-modal').classList.add('open')},children:`Bu Konsept"
js_content = js_content.replace(old_2, new_2)

# Just in case there's another variant of g(null, ...)
import re
js_content = re.sub(r'onClick:\(\)=>g\([^)]+\),children:`Bu Konsept', r"onClick:(e)=>{e.preventDefault();document.getElementById('whatsapp-modal').classList.add('open')},children:`Bu Konsept", js_content)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updates successful.")
