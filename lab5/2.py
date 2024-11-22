'''
Для каждой из трех заданных матриц найти среднее значение ее элементов
без учета максимального и минимального элементов. Полученные значения занести в одномерный массив.
Определить, образовали ли полученные значения убывающую или возрастающую последовательность.
Нахождение среднего значения элементов ма- трицы оформить в вид метода.
'''

A=[[34,2,3,54],
   [12,231,54,2],
   [0,11,1,276]]
B=[[11,12,54],
   [4,54,7]]
C=[[2,3],
   [75,12]]
D=[]
def aboba (M):
    S = 0
    a=len(M) #строки
    b=len(M[0]) #столбцы
    s=0 #сумма элементов
    maxim=M[0][0]
    minim=M[0][0]
    for i in range (a):
        for j in range (b):
            if M[i][j] > maxim:
                maxim = M[i][j]
            elif M[i][j] < minim:
                minim = M[i][j]
            S=S+M[i][j]
    S=S-maxim-minim
    N=a*b-2
    Sr=S/N
    return Sr
    return M

aboba(A)
aboba(B)
aboba(C)

D.append (aboba(A))
D.append (aboba(B))
D.append (aboba(C))

print ()

print ('МАТРИЦА А')
print('\n'.join('\t'.join(map(str, row)) for row in A))
print()
print ('МАТРИЦА В')
print('\n'.join('\t'.join(map(str, row)) for row in B))
print()
print ('МАТРИЦА С')
print('\n'.join('\t'.join(map(str, row)) for row in C))
print()
print ('СПИСОК СРЕДНИХ ЗНАЧЕНИЙ ЭЕЛЕМЕНТОВ МАТРИЦЫ')
print (D)
print ()
print ('ПОСЛЕДОВАТЕЛЬНОСТЬ')
if D[0]>D[1] and D[1]>D[2]:
    print ('Убывающая')
if D[0] < D[1] and D[1] < D[2]:
    print('Возрастающая')

'''
Если 
A=[[34,2,3,54],
   [12,231,54,2],
   [0,11,1,276]]
B=[[11,12,54],
   [4,54,7]]
C=[[2,3],
   [75,12]]
То D=[40.4, 21.0, 7.5]
Убывающая

Если
A=[[1 ,2 ,3,7 ],
   [2 ,91,8,12],
   [10,11,1,23]]
B=[[1,2,3],
   [40,50,70]]
C=[[29,23],
   [71,82]]
То D=[7.9, 23.75, 50.0]
Возрастающая

ВСЕ ВЕРНО, я проверила)
'''