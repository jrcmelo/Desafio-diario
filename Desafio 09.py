'''
Desenvolva uma função que receba um ano e determine se ele é bissexto ou não. A função deve retornar True para anos bissextos e False para os demais. 
Considere as regras oficiais do calendário gregoriano.
'''

Ano = (float(input('Ano: ')))

if (Ano / 400).is_integer():
    print ('É')
else:
    print ('Não é')