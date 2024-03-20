"""
n = int(input())
result = 0
for hour in range(0,n+1):
    if("3" in str(hour)):
        result += 60 * 60
        continue
    for min in range(0,60):
        if("3" in str(min)):
            result += 60
            continue
        for sec in range(0, 60):
            if("3" in str(sec)):
                result +=1
print(result) 
"""

h = int(input())

count = 0

for i in range(h+1):
    for j in range(60): 
        for k in range(60):
            if ('3' in str(i) + str(j) + str(k)):
                count += 1
print(count)