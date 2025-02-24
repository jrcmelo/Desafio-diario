'''
Faça uma função que tenha como entrada um range de números e retorne uma lista com todos os numeros pares desse range.
'''
def identificarnmpar (nm):
    pares = []

    for x in range(nm+1):
        if x%2==0:
            pares.append(x)
    return(pares)

numero = int(input('Digite um numero: '))
par = identificarnmpar(numero)
print(par)