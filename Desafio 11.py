'''
Crie uma função que receba uma lista de números inteiros e retorne a lista ordenada em ordem crescente,
mas com a seguinte condição: os números múltiplos de 3 devem aparecer primeiro, seguidos pelos números múltiplos de 5,
e por último os números que não são múltiplos nem de 3 nem de 5.
'''
def ordenar(lista):
    multiplos_3 = sorted([x for x in lista if x % 3 == 0])
    multiplos_5 = sorted([x for x in lista if x % 5 == 0 and x % 3 != 0])
    outros = sorted([x for x in lista if x % 3 != 0 and x % 5 != 0])
    
    lista_ord = multiplos_3 + multiplos_5 + outros
    return lista_ord


lista = [3, 7, 12, 19, 25, 31, 44, 58, 63, 77]

resultado = ordenar(lista)
print(resultado)