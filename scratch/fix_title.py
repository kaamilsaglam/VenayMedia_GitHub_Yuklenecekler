import re
import codecs

filepath = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'

with codecs.open(filepath, 'r', 'utf-8', errors='ignore') as f:
    content = f.read()

# The text is currently something like children:[`Fikirlerin Karanlktaki I`]
# We want to replace it with children:[`Fikirlerin Karanlıktaki Işığı`]

# Find the hero-title children
pattern = r'className:`hero-title text-gradient`,children:\[`Fikirlerin[^`]*`\]'
replacement = 'className:`hero-title text-gradient`,children:[`Fikirlerin Karanlıktaki Işığı`]'

new_content = re.sub(pattern, replacement, content)

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(new_content)

print("Title fixed.")
