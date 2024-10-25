import random
import math
random.seed (11)
x1=random.randint (1,15)
x2=random.randint (1,20)
x3=random.randint (1,14)
print (x1, '- номер 1-ого уровня; ',x2, '- номер 2-ого уровня',x3, '- номер 3-ого уровня')
print ()
s=0
a=int(input("Введите 1 элемент массива "))
b=int(input("Введите 2 элемент массива "))
c=int(input("Введите 3 элемент массива "))
d=int(input("Введите 4 элемент массива "))
e=int(input("Введите 5 элемент массива "))
f=int(input("Введите 6 элемент массива "))
h=[a, b, c, d, e, f]
print (h, 'это ваш массив')
for i in h:
    if i<0:
        s=s+1
if s<0:
    print ('ОШИБКААА')
print ('Число отрицательных элементов массива равно ', s)

    
    

