import codecs
import re

filepath = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(filepath, 'r', 'utf-8', errors='ignore') as f:
    content = f.read()

# We need to replace the old instagram grid array
old_array = '["./assets/ig_posts/post_new.jpg", "./assets/ig_posts/post_0.png", "./assets/ig_posts/post_2.jpg", "./assets/ig_posts/post_new_4.jpg"]'
new_array = '["./assets/insta0.png", "./assets/ig_posts/post_0.png", "./assets/ig_posts/post_new.jpg", "./assets/ig_posts/post_2.jpg", "./assets/ig_posts/post_new_4.jpg"]'

new_content = content.replace(old_array, new_array)

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(new_content)

print("Grid updated")
