import codecs

filepath = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-3nv5kxFG.js'
with codecs.open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target1 = "Konum: Konya, Selçuklu"
replacement1 = "Konya, Selçuklu"
content = content.replace(target1, replacement1)

target2 = "children:[`Fikirlerin`,(0,E.jsx)(`br`,{}),`Karanlıktaki Işığı`]"
replacement2 = "children:[`Fikirlerin Karanlıktaki Işığı`]"
content = content.replace(target2, replacement2)

with codecs.open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced successfully!")
