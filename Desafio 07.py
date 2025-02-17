'''
Faça uma função que pegue duas matrizes e tenha como resultado a soma delas. Por exemplo: duas matrizes 2x2, as duas tenho 2, 2, 2, 2, o resultado da função será 4, 4, 4, 4
'''
matriz1 = [
    [2, 2],
    [2, 2]
]

matriz2 = [
    [2, 2],
    [2, 5]
]

resultado = [
    [0, 0],
    [0, 0]
]


def soma_matriz():
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]

# Executando a soma
soma_matriz()

# Exibindo o resultado após a soma
for linha in resultado:
    print(linha)