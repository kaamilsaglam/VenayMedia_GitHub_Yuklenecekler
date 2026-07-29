import codecs
import re

filepath = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target_array = "[`VEN`,(0,E.jsx)(`span`,{className:`special-a`,children:`A`}),`Y`]"
content = content.replace(target_array, "`VENAY`")

# Replace the dotted version if it exists
content = content.replace("M E D İ A", "M E D I A")

# Also replace any stray occurrences if they exist
content = re.sub(r'M E D . A', 'M E D I A', content)

with codecs.open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced successfully!")
