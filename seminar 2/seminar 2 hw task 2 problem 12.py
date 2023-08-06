import os
os.system("cls")
s = float(input("input sum of numbers: "))
p = float(input("input product of numbers: "))
d=(s*s-4*p)
if d < 0: print("Petr made the mistake")
else:
    a = (s+d**0.5)/2
    b = s - a
    print("the answer is:",int(a), int(b))
