'''
Quero que você faça uma função que receba um número de 1 a 26 e me retorne um Array com as letras do alfabeto, então por exemplo eu escolhi 2
então eu quero que ele retorne um Array com a letra b.
'''

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def nmToText(numero):
    if numero < 27 and numero > 0:
        print(alfabeto[numero-1])
    else:
        print("Digite um numero valido!")

numero = int(input("Diga um numero de 1 a 26: "))
nmToText(numero)