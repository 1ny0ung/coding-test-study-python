import sys

"""
n = int(sys.stdin.readline().rstrip())
bag = -1

for five_kilo in range(n // 5, -1, -1):
    rest = n - five_kilo * 5
    if (rest % 3 == 0):
        bag = five_kilo + rest // 3
        break

print(bag)
"""

### 5로 나누어 떨어질 때 탈출하는 코드가 3으로 나누어 떨어질 때 코드보다 빠른 것 같음. 
n = int(sys.stdin.readline().rstrip())
bag = 0

while(n >= 0):
    if(n % 5 == 0):
        bag += n // 5
        break
    n -= 3
    bag += 1
else:
    bag = -1
print(bag)



