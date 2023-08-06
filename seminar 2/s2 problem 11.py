import os
os.system("cls")
n = input("enter a number greater than 1: ")
fib1, fib2, new_fib, i = 1, 1, 2, 3
if n.isdigit():
    n = int(n)
    if n > 1 :
        while new_fib < n:
            fib2 = fib1 + fib2
            fib1 = fib2 - fib1
            new_fib = fib1 + fib2
            i+=1
        if n == new_fib: 
            print(n," is Fibbonacci number, №= ",i, sep="")
        else: print(-1)
    else: print("it's not a number greater than 1")

else:
    print("it's not a number greater than 1")