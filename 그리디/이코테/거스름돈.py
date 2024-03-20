n = int(input())
count = 0
charge = [500, 100, 50, 10]
for coin in charge:
    count += n // coin
    n  %= coin
print(count)