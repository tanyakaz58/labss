'''
Вычислить значение функции y при заданном значении аргумента x по формуле
y=0, если |x|>=1, или y=x**2-1, если |x|<1
'''

import random
import math
random.seed (11)
x1=random.randint (1,10)
x2=random.randint (1,13)
print (x1, '- номер 1-ого уровня; ',x2, '- номер 2-ого и 3-его уровня')
print ()
x=int(input('Введите значение X '))
if math.fabs(x)<1:
    y=0
else:
    y=x**2-1
print (y)
    


