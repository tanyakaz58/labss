'''
В соревнованиях участвуют n спортсменов. Вывести на экран лучший результат.
'''

import random
import math
random.seed (11)
x1=random.randint (1,10)
x2=random.randint (1,13)
print (x1, '- номер 1-ого уровня; ',x2, '- номер 2-ого и 3-его уровня')
print ()
m=1000
n=int(input('Введите количество участников '))
a=n+1
for i in range (1,a): 
    h=float(input('Введите результат участника; если есть дробная часть, вводите ее через точку '))
    if h<m:
        m=h
print (m)
        
