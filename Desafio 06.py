'''
Implemente uma função que receba um número inteiro positivo X e exiba um triângulo retângulo na tela, onde a base e a altura tenham X caracteres de largura. 
O triângulo deve ser formado por * e crescer linha a linha.
'''

Base = int (input())
i = 1

while i <= Base:
  print('*' * i)
  i += 1