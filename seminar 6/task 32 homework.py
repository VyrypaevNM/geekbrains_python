# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import os, random
os.system("cls")
num = int(input("input number of elements = "))
low = int(input("input low border = "))
high = int(input("input high border = "))
a = [random.randint(0,100) for i in range(num)]
print (a)
for indx in range(num):
    if (a[indx]>low or a[indx] == low) and (a[indx]<high or a[indx]==high): 
        print(indx)
