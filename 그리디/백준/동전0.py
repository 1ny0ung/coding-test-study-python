n, k = map(int, input().split())
coin_values = list()
for i in range(0, n):
    coin_values.append(int(input()))
coin_values.sort(reverse=True)

result = 0
for coin in coin_values:
    if(k == 0):
        break
    result += k // coin 
    k = k % coin
print(result)