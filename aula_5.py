import re

cpf = '147.852.963-12'
regex_CPF = re.findall(r'(([0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf)

# print(regex_CPF)

texto = '<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>'
substituindo_coisas = re.sub(r'(<(.+?)>)(.+?)(</\2>)', r'\1 \3 lla \4', texto)
print(substituindo_coisas)