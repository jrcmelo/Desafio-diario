import math

a = float (input('A: '))
b = float (input('B: '))
c = float (input('C: '))

D = ((b*b)-4*a*c)

X1 = (b+math.sqrt(D))/(2*a)
X2 = (b-math.sqrt(D))/(2*a)

print ('X1: ', X1, ', X2: ', X2)