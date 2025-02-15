'''
Faça uma função que criptografe um texto, recebendo um texto e retorne uma criptografia que transforme as letras em sua respectiva colocação no alfabeto. 
Por exemplo, "mamaco" vira "13 1 13 1 3 15"
'''

nmToletter = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

def cript(text):
    i = 0
    while i < len(text):
        print(nmToletter[text[i]], end=" ")
        i+=1

text = input("Digite um texto: ")
cript(text.upper())