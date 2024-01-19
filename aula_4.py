import re

texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>    
'''

pegar_tags = re.findall(r'<[pdiv]{1,3}>', texto)