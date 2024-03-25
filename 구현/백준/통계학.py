"""
n = int(input())
num : list[int] = list()
for i in range(0, n):
    num.append(int(input()))
num.sort()
avg = round(sum(num) / n)
median = num[n//2]
range_min_max = num[n-1] - num[0]

count_list= [0] * n
j = 0
while(j < n-1):
    count = num.count(num[j])
    if (count > 1): 
        count_list[j] = count
        j += count
    else:
        j += 1
max = max(count_list)
index = count_list.index(max)
if (count_list.count(max) > 1):
    for i in range(index+1, n):
        if (count_list[i] == max):
            index = i
            break
mode = num[index]
print(avg)
print(median)
print(mode)
print(range_min_max)
"""
n = int(input())
num : list[int] = list()
for i in range(0, n):
    num.append(int(input()))
num.sort()
avg = round(sum(num) / n)
median = num[n//2]
range_min_max = num[n-1] - num[0]
mode : int

count_dict = dict()
for number in num:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

key_list = [key for key, value in count_dict.items() if (value == max(count_dict.values()))]
if(len(key_list) == 1):
    mode = key_list[0]
else:
    mode = key_list[1]
print(avg)
print(median)
print(mode)
print(range_min_max)