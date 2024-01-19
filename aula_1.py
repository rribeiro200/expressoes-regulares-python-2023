import re

string = 'Este é um teste de expressões regulares'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ABCD', string, count=1))
print(string)

regexp = re.compile(r'teste')
regexp.search(string)
regexp.findall(string)
regexp.sub('DEF', string)