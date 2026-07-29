import codecs
import re
import os

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')
css_path = os.path.join(base_dir, 'assets', 'index-sFkQ3OzH.css')
html_path = os.path.join(base_dir, 'index.html')

# 1. Update JS
with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Change href from wa.me to #whatsapp-modal in the button
js_content = re.sub(
    r"href:`https://wa\.me/905555555555.*?`",
    r"href:`#whatsapp-modal`",
    js_content
)
# We also need to remove target="_blank" and rel from the react button if possible, but it won't hurt to keep them if they don't break anything. 
# Better yet, replace the whole href/target/rel chunk:
js_content = re.sub(
    r"href:`#whatsapp-modal`,target:`_blank`,rel:`noopener noreferrer`",
    r"href:`#whatsapp-modal`",
    js_content
)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

# 2. Update CSS
with codecs.open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_addition = """
.wa-modal-overlay {
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  z-index: 2000;
  opacity: 0;
  visibility: hidden;
  width: 100%;
  height: 100%;
  transition: var(--transition-normal);
  background: #000000d9;
  justify-content: center;
  align-items: center;
  display: flex;
  position: fixed;
  top: 0;
  left: 0;
}
.wa-modal-overlay.open {
  opacity: 1;
  visibility: visible;
}
.wa-modal-content {
  background: var(--color-bg-surface);
  width: 90%;
  max-width: 400px;
  border: 1px solid #d4af3726;
  border-radius: 16px;
  padding: 2.5rem 2rem;
  position: relative;
  transform: translateY(30px) scale(.95);
  transition: var(--transition-normal);
  box-shadow: 0 20px 60px #000c;
  text-align: center;
}
.wa-modal-overlay.open .wa-modal-content {
  transform: translateY(0) scale(1);
}
.wa-modal-close {
  color: var(--color-text-secondary);
  cursor: pointer;
  width: 36px;
  height: 36px;
  transition: var(--transition-fast);
  background: #00000080;
  border: none;
  border-radius: 50%;
  font-size: 1.5rem;
  position: absolute;
  top: 1rem;
  right: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
.wa-modal-close:hover {
  color: var(--color-accent-gold);
  background: #000c;
}
.wa-modal-header h3 {
  font-family: var(--font-secondary);
  color: var(--color-accent-gold);
  font-size: 1.8rem;
  margin-bottom: 0.5rem;
}
.wa-modal-header p {
  color: var(--color-text-secondary);
  font-size: 0.95rem;
  margin-bottom: 2rem;
}
.wa-contact-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.wa-contact-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  background: #ffffff0d;
  border: 1px solid #ffffff1a;
  border-radius: 12px;
  padding: 1rem;
  text-decoration: none;
  transition: var(--transition-fast);
  color: var(--color-text-primary);
}
.wa-contact-btn:hover {
  background: #d4af3726;
  border-color: var(--color-accent-gold);
  transform: translateY(-2px);
}
.wa-contact-info {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.wa-name {
  font-family: var(--font-primary);
  font-weight: 700;
  font-size: 1.1rem;
}
.wa-role {
  font-size: 0.85rem;
  color: var(--color-accent-gold);
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-top: 0.2rem;
}
"""

if '.wa-modal-overlay' not in css_content:
    css_content += css_addition
    with codecs.open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

# 3. Update HTML
with codecs.open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Fix the floating whatsapp link
html_content = re.sub(
    r'href="https://wa\.me/905555555555.*?"',
    r'href="#whatsapp-modal"',
    html_content
)

# Add Modal HTML and script
modal_html = """
    <div class="wa-modal-overlay" id="whatsapp-modal">
      <div class="wa-modal-content">
        <button class="wa-modal-close" onclick="document.getElementById('whatsapp-modal').classList.remove('open')">&times;</button>
        <div class="wa-modal-header">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="45" height="45" fill="#25D366" style="margin-bottom:15px;"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
          <h3>Kiminle görüşmek istersiniz?</h3>
          <p>Lütfen iletişim kurmak istediğiniz yöneticimizi seçin.</p>
        </div>
        <div class="wa-contact-list">
          <a href="https://wa.me/905307221327?text=Merhaba,%20Venay%20Media%27n%C4%B1n%20%C3%A7al%C4%B1%C5%9Fmalar%C4%B1n%C4%B1%20inceledim.%20Hayalimizdeki%20konsept%20i%C3%A7in%20sizinle%20g%C3%B6r%C3%BC%C5%9Fmek%20ve%20detayl%C4%B1%20bilgi%20almak%20istiyorum." target="_blank" class="wa-contact-btn">
            <div class="wa-contact-info">
              <span class="wa-name">Yasin Sarısakal</span>
              <span class="wa-role">Yönetici</span>
            </div>
          </a>
          <a href="https://wa.me/905346652018?text=Merhaba,%20Venay%20Media%27n%C4%B1n%20%C3%A7al%C4%B1%C5%9Fmalar%C4%B1n%C4%B1%20inceledim.%20Hayalimizdeki%20konsept%20i%C3%A7in%20sizinle%20g%C3%B6r%C3%BC%C5%9Fmek%20ve%20detayl%C4%B1%20bilgi%20almak%20istiyorum." target="_blank" class="wa-contact-btn">
            <div class="wa-contact-info">
              <span class="wa-name">Yusuf Zengin</span>
              <span class="wa-role">Yönetici</span>
            </div>
          </a>
          <a href="https://wa.me/905413661600?text=Merhaba,%20Venay%20Media%27n%C4%B1n%20%C3%A7al%C4%B1%C5%9Fmalar%C4%B1n%C4%B1%20inceledim.%20Hayalimizdeki%20konsept%20i%C3%A7in%20sizinle%20g%C3%B6r%C3%BC%C5%9Fmek%20ve%20detayl%C4%B1%20bilgi%20almak%20istiyorum." target="_blank" class="wa-contact-btn">
            <div class="wa-contact-info">
              <span class="wa-name">Recep Aslan</span>
              <span class="wa-role">Yönetici</span>
            </div>
          </a>
        </div>
      </div>
    </div>
    
    <script>
      document.addEventListener('click', function(e) {
        var target = e.target.closest('a');
        if (target && target.getAttribute('href') === '#whatsapp-modal') {
          e.preventDefault();
          document.getElementById('whatsapp-modal').classList.add('open');
        }
      });
    </script>
"""

if 'id="whatsapp-modal"' not in html_content:
    html_content = html_content.replace('</body>', modal_html + '\n  </body>')
    with codecs.open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

print("All done!")
