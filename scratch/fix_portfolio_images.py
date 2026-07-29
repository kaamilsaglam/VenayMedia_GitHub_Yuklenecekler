import codecs
import os

base_dir = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler'
js_path = os.path.join(base_dir, 'assets', 'index-3nv5kxFG.js')

with codecs.open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace Sinematik Hikayeler URL
old_url_1 = "https://images.unsplash.com/photo-1601506521937-0121a7fc2a6b?q=80&w=1000&auto=format"
new_url_1 = "./assets/ig_posts/post_new.jpg"
js_content = js_content.replace(old_url_1, new_url_1)

# Replace Ölümsüz Kareler URL
old_url_2 = "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?q=80&w=1000&auto=format"
new_url_2 = "./assets/ig_posts/post_third.jpg"
js_content = js_content.replace(old_url_2, new_url_2)

# Just to be extremely robust, replace the base URLs if the query string was different
js_content = js_content.replace("https://images.unsplash.com/photo-1601506521937-0121a7fc2a6b", new_url_1)
js_content = js_content.replace("https://images.unsplash.com/photo-1516035069371-29a1b244cc32", new_url_2)

with codecs.open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Updates successful.")
