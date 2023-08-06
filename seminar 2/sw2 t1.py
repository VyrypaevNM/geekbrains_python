import os
os.system("cls")
n = int(input("input positive number = "))
rez, i = 1, 1
#i = int(1)
while i<=n:
    rez *= i
    i+=1
print(n,"! = ",rez, sep="")
