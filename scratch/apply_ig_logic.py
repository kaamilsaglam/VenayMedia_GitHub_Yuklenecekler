import codecs
import re
import os

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
html_path = os.path.join(base_dir, 'index.html')

with codecs.open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Update static floating icon href just in case
html_content = html_content.replace('href="https://instagram.com"', 'href="https://www.instagram.com/venaymedia"')

# Add dynamic injection script before </body>
dom_script = """
    <script>
      setInterval(function() {
        // Standardize all Instagram links
        document.querySelectorAll('a[href*="instagram.com"]').forEach(function(a) {
          if (a.href !== "https://www.instagram.com/venaymedia") {
            a.href = "https://www.instagram.com/venaymedia";
          }
        });

        var igSvg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="22" height="22" style="vertical-align:middle;margin-right:8px"><defs><radialGradient id="ig-grad" r="150%" cx="30%" cy="107%"><stop offset="0%" stop-color="#fdf497"/><stop offset="5%" stop-color="#fdf497"/><stop offset="45%" stop-color="#fd5949"/><stop offset="60%" stop-color="#d6249f"/><stop offset="90%" stop-color="#285AEB"/></radialGradient></defs><path fill="url(#ig-grad)" d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>`;

        // Update Bizi Takip Edin button
        document.querySelectorAll('.btn-outline').forEach(function(btn) {
          if(btn.textContent.includes('Takip Edin') && !btn.innerHTML.includes('svg')) {
            btn.innerHTML = igSvg + btn.textContent;
            btn.style.display = 'inline-flex';
            btn.style.alignItems = 'center';
            btn.style.justifyContent = 'center';
          }
        });

        // Update Footer Social Link
        document.querySelectorAll('.footer-social .social-links a').forEach(function(a) {
          if(a.href.includes('instagram') && !a.innerHTML.includes('ig-grad')) {
            a.innerHTML = igSvg.replace('margin-right:8px', 'margin-right:0');
          }
        });
      }, 500);
    </script>
"""

if 'ig-grad' not in html_content:
    html_content = html_content.replace('</body>', dom_script + '\n  </body>')
    with codecs.open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

print("HTML updated for Instagram logos and links.")
