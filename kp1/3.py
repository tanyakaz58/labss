import numpy as np
m=0
x=np.array([1,2,5,4,7,3,9,10,10])
for i, val in enumerate(x):
    print (i, '– значение индекса элемента; ', val, '– значение элемента')
    if val>m:
        m=val
print ()
print (m, '- наибольшее значение элемента в массиве ')
print ()
for i, val in enumerate(x):
    z=np.array([i])
print (z, 'Массив из индексов максимальных элементов ')
    


