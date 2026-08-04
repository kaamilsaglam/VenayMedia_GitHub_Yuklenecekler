import codecs

filepath = r'c:\Users\Kamil\Desktop\VenayMedia_GitHub_Yuklenecekler\assets\index-sFkQ3OzH.css'

with codecs.open(filepath, 'r', 'utf-8') as f:
    css = f.read()

# Replace invalid animation timing function variable
css = css.replace('1s var(--transition-normal)', '1s cubic-bezier(.16, 1, .3, 1)')

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(css)

print("CSS animations fixed.")
