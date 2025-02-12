'''
Crie uma função que, ao receber três coeficientes a, b e c, gere e retorne uma string representando a equação do segundo grau no formato ax² + bx + c = 0.
'''

import math

a = float (input('A: '))
b = float (input('B: '))
c = float (input('C: '))

D = ((b*b)-4*a*c)

X1 = (b+math.sqrt(D))/(2*a)
X2 = (b-math.sqrt(D))/(2*a)

print(a,'x²+',b,'x+',c,' = 0')
print ('x1: ', X1, ', x2: ', X2)