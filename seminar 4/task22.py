import os
os.system("cls")
num1 = int(input("input first list's quantity = "))
num2 = int(input("input second list's quantity = "))
lst1=[]
lst2=[]

for i in range (num1):
    input_string = "list 1 element " + str(i)+ "= "
    temp = int(input(input_string))
    lst1.append(temp)

print()
for i in range (num2):
    input_string = "list 2 element " + str(i)+ "= "
    temp = int(input(input_string))
    lst2.append(temp)

print(set(lst1)& set(lst2))
lst1 = list(set(lst1))
lst2 = list(set(lst2))

print(lst1)