import os
os.system("cls")
n = int(input("input coins number: "))
coin_sum = 0

for i in range(n):
    message = "input coin № " + str(i+1)+" side ( 0 or 1): "
    coin_sum += int(input(message))

print(min(coin_sum, n-coin_sum),"coins needed to turn over")
