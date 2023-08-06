import os
os.system("cls")
n = input("input a positive number = ")
rez, i = 1, 1
if n.isdigit():
    n = int(n)
    if n >0 :
        while i<=n:
            rez *= i
            i+=1
        print(n,"! = ",rez, sep="")
    else: print("it's not a positive number")

else:
    print("it's not a positive number")
