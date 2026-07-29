import os

js_path = 'assets/index-3nv5kxFG.js'

with open(js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Splash logo
t1_old = '(0,E.jsx)(`div`,{className:`splash-logo text-gradient`,children:`VENAY MEDIA`})'
t1_new = '(0,E.jsxs)(`div`,{className:`splash-logo text-gradient logo-container`,children:[(0,E.jsxs)(`div`,{className:`logo-venay`,children:[`VEN`,(0,E.jsx)(`span`,{className:`special-a`,children:`A`}),`Y`]}),(0,E.jsx)(`div`,{className:`logo-media`,children:`M E D İ A`})]})'

# 2. Header logo
t2_old = '(0,E.jsx)(`a`,{href:`#`,className:`logo`,children:`VENAY MEDIA`})'
t2_new = '(0,E.jsxs)(`a`,{href:`#`,className:`logo logo-container`,children:[(0,E.jsxs)(`span`,{className:`logo-venay`,children:[`VEN`,(0,E.jsx)(`span`,{className:`special-a`,children:`A`}),`Y`]}),(0,E.jsx)(`span`,{className:`logo-media`,children:`M E D İ A`})]})'

# 3. Footer logo
t3_old = '(0,E.jsx)(`span`,{className:`logo`,children:`VENAY MEDIA`})'
t3_new = '(0,E.jsxs)(`span`,{className:`logo logo-container`,children:[(0,E.jsxs)(`span`,{className:`logo-venay`,children:[`VEN`,(0,E.jsx)(`span`,{className:`special-a`,children:`A`}),`Y`]}),(0,E.jsx)(`span`,{className:`logo-media`,children:`M E D İ A`})]})'

print('Splash replacement count:', content.count(t1_old))
print('Header replacement count:', content.count(t2_old))
print('Footer replacement count:', content.count(t3_old))

content = content.replace(t1_old, t1_new)
content = content.replace(t2_old, t2_new)
content = content.replace(t3_old, t3_new)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Replacements written to index-3nv5kxFG.js successfully!')
