import codecs
import os

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')
html_path = os.path.join(base_dir, 'index.html')

with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# 1. Update the images array in JS to remove the duplicate post_3 (which is the brown logo).
# So it becomes: post_new (brown logo at start), post_0, post_1, post_2.
# We also remove any other occurrences of post_3 if they exist.
js_content = js_content.replace(
    '["./assets/ig_posts/post_new.jpg", "./assets/ig_posts/post_0.png", "./assets/ig_posts/post_1.jpg", "./assets/ig_posts/post_2.jpg", "./assets/ig_posts/post_3.jpg"]',
    '["./assets/ig_posts/post_new.jpg", "./assets/ig_posts/post_0.png", "./assets/ig_posts/post_1.jpg", "./assets/ig_posts/post_2.jpg"]'
)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

# 2. Update index.html script to robustly replace IG
with codecs.open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# We'll completely replace the old DOM update script block with a new, more robust one.
new_script = """
    <script>
      setInterval(function() {
        // Standardize all Instagram links
        document.querySelectorAll('a[href*="instagram.com"]').forEach(function(a) {
          if (a.href !== "https://www.instagram.com/venaymedia") {
            a.href = "https://www.instagram.com/venaymedia";
          }
        });

        var igSvg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="22" height="22" style="vertical-align:middle;margin-right:8px"><defs><radialGradient id="ig-grad" r="150%" cx="30%" cy="107%"><stop offset="0%" stop-color="#fdf497"/><stop offset="5%" stop-color="#fdf497"/><stop offset="45%" stop-color="#fd5949"/><stop offset="60%" stop-color="#d6249f"/><stop offset="90%" stop-color="#285AEB"/></radialGradient></defs><path fill="url(#ig-grad)" d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>`;
        var igSvgBig = igSvg.replace('width="22" height="22"', 'width="36" height="36"').replace('margin-right:8px', 'margin-right:0');

        // Update Takip Et button (removes IG)
        document.querySelectorAll('.btn-outline').forEach(function(btn) {
          if(btn.textContent.includes('Takip Et') && !btn.innerHTML.includes('svg')) {
            btn.innerHTML = igSvg + 'Takip Et';
            btn.style.display = 'inline-flex';
            btn.style.alignItems = 'center';
            btn.style.justifyContent = 'center';
          }
        });

        // Update IG overlays
        document.querySelectorAll('.ig-overlay div').forEach(function(div) {
          if (div.textContent.trim() === 'IG') {
            div.innerHTML = igSvgBig;
          }
        });

        // Update Footer Social Link (removes IG)
        document.querySelectorAll('.footer-social .social-links a').forEach(function(a) {
          if(a.href.includes('instagram') && !a.innerHTML.includes('ig-grad')) {
            a.innerHTML = igSvg.replace('margin-right:8px', 'margin-right:0');
          }
        });
      }, 500);
    </script>
"""

# Find where to replace in html
import re
# We'll replace everything from <script> setInterval(function() { // Standardize all Instagram links to </script>
html_content = re.sub(r'<script>\s*setInterval\(function\(\) \{\s*// Standardize all Instagram links.*?</script>', new_script.strip(), html_content, flags=re.DOTALL)

with codecs.open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updates successful.")
