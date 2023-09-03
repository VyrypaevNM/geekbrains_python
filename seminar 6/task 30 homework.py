# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

import os
os.system("cls")
first_elem = int(input("input first element= "))
a = [first_elem]
diff = int(input("input difference= "))
num = int(input("input number of elements= "))
temp = first_elem
for i in range(num-1):
    temp += diff
    a.append(temp)
print(a)
