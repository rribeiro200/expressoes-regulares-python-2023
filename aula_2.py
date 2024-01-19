# Meta caracteres = . ^ $ * + ? { } [ ] \ | ( )
# | = OU
# . = Qualquer caractere (com exceção da quebra de linha)
# [] = Conjunto de caracteres

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

procura_joao_e_maria = re.findall(r'João|Maria', texto)
conjunto_de_caracteres = re.findall(r'[Jj]o[aã]o|[Mm]aria', texto)
range_de_caracteres = re.findall(r'[a-zA-Z]aria|[a-zA-Z]o[aã]o', texto)
ignore_case = re.findall(r'jOãO|mAriA|não', texto, flags=re.IGNORECASE)

# print(procura_joao_e_maria)
# print(conjunto_de_caracteres)
# print(range_de_caracteres)
print(ignore_case)