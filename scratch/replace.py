import codecs

filepath = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target = "`VENAY`"
replacement = "[`VEN`,(0,E.jsx)(`span`,{className:`special-a`,children:`A`}),`Y`]"
content = content.replace(target, replacement)

with codecs.open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored successfully!")
