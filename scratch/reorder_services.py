import codecs
import os
import re

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
html_path = os.path.join(base_dir, 'index.html')

with codecs.open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Script to inject for reordering
order_script = """
        // Reorder services grid
        var servicesGrid = document.querySelector('.services-grid');
        if (servicesGrid) {
          Array.from(servicesGrid.children).forEach(function(card) {
            var text = card.textContent;
            if (text.includes('Medya')) card.style.order = '1';
            else if (text.includes('Marka')) card.style.order = '2';
            else if (text.includes('Düğün')) card.style.order = '3';
            else if (text.includes('Kına')) card.style.order = '4';
          });
        }
"""

if 'Reorder services grid' not in html_content:
    html_content = html_content.replace('// Update Footer Social Link', order_script + '\n        // Update Footer Social Link')

with codecs.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updates successful.")
