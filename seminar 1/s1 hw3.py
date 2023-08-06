n=923455
n1=n%1000
n2=n//1000
print("yes" if ((n1%10+n1//100+n1//10%10)==(n2%10+n2//100+n2//10%10)) else "no")
print(n1,n2)


a = 2
print("А равна 1" if a == 1 else "А не равна 1")
