'''
Одноклеточная амеба каждые 3 ч делится на 2 клетки. Определить через какое время в замкнутом объеме будет находиться 10^5 клеток, если первоначально
в замкнутом объеме находилось 10 клеток.
'''

a=10
b=10**5
c=3
d=0
while a<b:
    a=a*2
    d=d+3
print (d)
