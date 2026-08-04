import codecs

filepath = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-sFkQ3OzH.css'

with codecs.open(filepath, 'a', 'utf-8') as f:
    f.write('\n.hero-title.text-gradient { animation: fadeInUp 1s var(--transition-normal) .2s both, shine 4s linear infinite; }\n')

print("Animation combined.")
