'''
Если максимальный среди элементов с четными индексами
больше максимального среди элементов с нечетными индексами, то
заменить нулями элементы первой половины массива, иначе — эле-
менты второй половины.
'''
import random
random.seed (11)
x1=random.randint (1,15)
x2=random.randint (1,20)
x3=random.randint (1,14)
print (x1, '- номер 1-ого уровня; ',x2, '- номер 2-ого уровня;',x3, '- номер 3-ого уровня')
print ()

x=[109,0,53]
l=len(x)
ch=[]
nch=[]
k=l-1

for i in range (l):
    if i%2==0:
        ch.append (x[i])
    else:
        nch.append (x[i])
print('Четные ', ch)
print ('Нечетные ', nch)

print()

a=max (ch)
b=max (nch)
print ('Максимальное из чисел с четными индексами ', a)
print ('Максимальное из чисел с нечетными индексами ', b)

print()

if a > b:
    for i in range(l // 2):
      x[i] = 0
else:
    for i in range((l + 1) // 2, l):
      x[i] = 0
print ('Измененный массив ', x)

'''
Если массив x=[14,1,56,589,2,90]
Максимальное из чисел с четными индексами 56
Максимальное из чисел с нечетными индексами 589
Измененный массив [14, 1, 56, 0, 0, 0]

Если массив x=[109,0,53]
Максимальное из чисел с четными индексами 109
Максимальное из чисел с нечетными индексами 0
Измененный массив [0,0,53]
'''

    