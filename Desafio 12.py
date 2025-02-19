'''
"Crie uma função que receba uma string e retorne True se ela for um palíndromo e False caso contrário. 
Um palíndromo é uma palavra ou frase que pode ser lida da mesma forma de trás para frente, ignorando espaços e diferenciação entre maiúsculas e minúsculas.

Exemplos:
✅ 'Ama a ama' → True
✅ 'Python' → False
✅ 'Anotaram a data da maratona' → True
'''

def palindromo(frase):
    # print(' Você digitou: {}'.format(frase))
    invertida = ' '.join(palavra.lstrip()[::-1] for palavra in frase.split())
    if invertida == frase:
        print('✅')
    else:
        print('❌')
    # print('A frase que você digitou invertida fica: {}'.format(invertida.lstrip()))

frase = input('Digite uma frase: ')
palindromo(frase.lower())