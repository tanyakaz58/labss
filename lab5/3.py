'''
Вычислить суммы по формулам:
s=1+E cos(ix)/i! ; y=e**(cos(x))*cos(sin(x)) ; a=0.1, b=1, h=0.1
s=E ((-1)**i)*cos(ix)/i**2 ; y=(x**2-((pi**2)/3))/4 ; a=pi/5 ; b=pi ; h= pi/25
Простите за страшные формулы...
'''
import math
import numpy as np

def summ (x):
    s=1
    i=1
    k=math.cos(i*x)/math.factorial(i)
    while k>0.0001:
        s=s+a
        i=i+1
        k=math.cos(i*x)/math.factorial(i)
    return s
a=0.1
b=1
h=0.1
print()
print ('ДЛЯ СУММЫ ПО ПЕРВОЙ ФОРМУЛЕ')
for x in np.arange (a,b,h):
    y=(math.e**(math.cos(x)))*math.cos(math.sin(x))
    s=summ(x)
    print ('x =', x, 'y =', y, 's =', s)

print()

def summ1 (x):
    s=0
    i=1
    k=((-1)**i)*(math.cos(i*x))/(i**2)
    while k>0.0001:
        s=s+a
        i=i+1
        k=((-1)**i)*(math.cos(i*x))/(i**2)
    return s
a=math.pi/5
b=math.pi
h=math.pi/25
print('ДЛЯ СУММЫ ПО ВТОРОЙ ФОРМУЛЕ')
for x in np.arange (a,b,h):
    y=(x**2-((math.pi**2)/3))/4
    s=summ1(x)
    print ('x =', x, 'y =', y, 's =', s)