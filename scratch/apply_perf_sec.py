import codecs
import re

print("Starting security and performance modifications...")

# 1. Update HTML
html_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\index.html'
with codecs.open(html_path, 'r', 'utf-8', errors='ignore') as f:
    html = f.read()

# Fix corrupted description
bad_desc = '<meta name="description" content="Venay Media, fikirlerin karanlktaki . Dn organizasyonu, kna organizasyonu ve profesyonel medya & ekim hizmetleri." />'
good_desc = '<meta name="description" content="Venay Media, fikirlerin karanlıktaki ışığı. Düğün organizasyonu, kına organizasyonu ve profesyonel medya & çekim hizmetleri." />'
if bad_desc in html:
    html = html.replace(bad_desc, good_desc)
else:
    # Regex fallback if exact string mismatch
    html = re.sub(r'<meta name="description" content="[^"]+" />', good_desc, html)

# Add Security Headers if not present
security_tags = """
    <meta http-equiv="Content-Security-Policy" content="default-src 'self' 'unsafe-inline' 'unsafe-eval' https: data:; img-src 'self' https: data:;">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">"""
if "Content-Security-Policy" not in html:
    html = html.replace('<meta name="viewport"', security_tags.strip() + '\n    <meta name="viewport"')

# Bump cache to v9
html = re.sub(r'v=\d+', 'v=9', html)

with codecs.open(html_path, 'w', 'utf-8') as f:
    f.write(html)
print("HTML updated.")


# 2. Update CSS
css_path = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-sFkQ3OzH.css'
with codecs.open(css_path, 'r', 'utf-8', errors='ignore') as f:
    css = f.read()

perf_css = """
/* Performance & Mobile Fluidity */
* {
  -webkit-tap-highlight-color: transparent;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.hero-title, .portfolio-item, .ig-post, .btn {
  transform: translateZ(0);
  will-change: transform, opacity;
  backface-visibility: hidden;
}
/* Mobile Click Animation */
a, button, .ig-post, .portfolio-item {
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
a:active, button:active, .ig-post:active, .portfolio-item:active {
  transform: scale(0.96) !important;
}
"""

if "-webkit-tap-highlight-color: transparent" not in css:
    css += perf_css

with codecs.open(css_path, 'w', 'utf-8') as f:
    f.write(css)
print("CSS updated.")
