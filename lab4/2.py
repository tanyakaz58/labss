'''
Дана матрица А размером 5х7. Для каждой строки сравнить элементы,
расположенные непосредственно перед и после максимального
элемента этой строки, и меньший из них увеличить в 2 раза.
Если максимальный элемент является первым или последним в строке,
то увеличить в 2 раза только один соседний элемент.
'''
a=[[1,2,3,4,5,6,7],[7,6,5,4,3,2,1],[2,3,4,5,6,7,8],[8,7,6,5,4,3,2],[9,8,7,6,5,4,3]]
for i in range (5):
    maxi=a[i][0]
    ind=0
    for j in range (7):
        if maxi<a[i][j]:
            maxi=a[i][j]
            ind=j
    if ind==0:
        a[i][1]=int(a[i][1]*2)
    elif ind==6:
        a[i][5]=int(a[i][5]*2)
    else:
        if a[i][ind-1]<=a[i][ind+1]:
            a[i][ind-1]=a[i][ind-1]*2
        else:
            a[i][ind+1]=a[i][ind+1]*2
print(a)
'''
Если матрица [[1,2,3,4,5,6,7],[7,6,5,4,3,2,1],[2,3,4,5,6,7,8],[8,7,6,5,4,3,2],[9,8,7,6,5,4,3]]
То выведет [[[1,2,3,4,5,12,7],[7,12,5,4,3,2,1],[2,3,4,5,6,14,8],[8,14,6,5,4,3,2],[9,16,7,6,5,4,3]]]
Все верно

Если матрица [[12,23,12,56,4,6,8],[6,43,23,65,76,3,2],[34,98,67,56,43,34,3],[23,12,43,5,2,1,6],[3,1,4,5,7,8,5]]
То выведет [[12, 23, 12, 56, 8, 6, 8], [6, 43, 23, 65, 76, 6, 2], [68, 98, 67, 56, 43, 34, 3], [23, 12, 43, 10, 2, 1, 6], [3, 1, 4, 5, 7, 8, 10]]
Все верно
'''
