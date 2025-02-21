'''
Crie uma função que receba uma data no formato dd/mm/aaaa e determine se ela é uma data válida ou não. A função deve verificar se:

O dia está dentro do intervalo válido para o mês e ano informado.
O mês está entre 1 e 12.
O ano é válido (qualquer número maior que 0).
Se o ano for bissexto, fevereiro pode ter até 29 dias.
Se a data for válida, retorne True. Caso contrário, retorne False.
'''
import datetime
import os

def Validar(data):
    while True:
        try:
            os.system('cls')
            Data = datetime.datetime.strptime(data, "%d/%m/%Y")
            print(Data.strftime("%d"+'/'+"%m"+'/'+"%Y"+' É uma data valida!'))
            break
        except ValueError:
            os.system('cls')
            print(data + " Não é uma data valida! Tente de novo")
            data = input('\nDigite uma data. \nEx: 30/02/2025 \n')

data = input('Digite uma data, \nEx: 30/02/2025 \n')
Validar(data)