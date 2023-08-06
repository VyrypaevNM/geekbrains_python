import os
os.system("cls")
n = int(input("input positive number: "))
i = 0
rez=1
while rez <= n:
    print(rez)
    i += 1
    rez = 2 ** i