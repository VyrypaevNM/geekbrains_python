data = 'rara-ra rarra papaa paso-a'
data1 = list(map(str,data.split()))

print(data1)
temp_bool = True
temp = 0
indx = 0

for x in data1:
    counter = 0
    for c in x:
        if c in "euioa":
            counter += 1
    if indx >0 : 
        temp_bool = (temp_bool & (temp == counter))
    temp = counter
    indx += 1
   
print("param pam-pam" if temp_bool else "pam param")