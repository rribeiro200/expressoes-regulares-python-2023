# Meta caracteres = ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
# {min, max}
# {10, } 10 ou mais
# {, 10} De zero a 10
# {10} Especificamente 10
# {5, 10} De 5 a 10
# ()+ [a-zA-Z0-9]+

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

repetindo_caractere_1_ou_N_vezes = re.findall(r'jo+ão+', texto, flags=re.I)
substituindo = re.sub(r'jo+ão+', 'Felipe', texto, flags=re.I)
quantificador = re.findall(r've{0,10}m{1,2}', texto, flags=re.I)

# print(repetindo_caractere_1_ou_N_vezes)
# print(substituindo)
# print(quantificador)

texto2 = 'João ama ser amado'
quantificador_2 = re.findall(r'ama[do]{0,}', texto2, flags=re.I)
print(quantificador_2)