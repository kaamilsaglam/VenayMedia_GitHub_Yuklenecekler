import codecs
import os
import re

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
html_path = os.path.join(base_dir, 'index.html')

with codecs.open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

new_block = """document.querySelectorAll('.btn, .btn-primary, .wa-button, a, button').forEach(function(btn) {
          var text = (btn.textContent || '').toUpperCase();
          if (text.includes('RANDEVU') || btn.classList.contains('wa-button')) {
            if(btn.tagName.toLowerCase() === 'a') btn.href = '#whatsapp-modal';
            
            if (!btn.dataset.waBound) {
              btn.dataset.waBound = 'true';
              btn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                e.stopImmediatePropagation();
                document.getElementById('whatsapp-modal').classList.add('open');
              }, true);
            }
          }
        });"""

# We need to replace the old block starting with document.querySelectorAll('.btn, .btn-primary... 
# until the end of the forEach block.
html_content = re.sub(r'document\.querySelectorAll\(\'\.btn, \.btn-primary.*?\}\);', new_block, html_content, flags=re.DOTALL)

with codecs.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updates successful.")
