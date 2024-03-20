"""
n = int(input())
fear_array = list(map(int, input().split()))
result = 0

fear_array.sort()
index = 0
while (True):
    num = fear_array[index]
    if(num <= n):
        if(index >= num):
            result += 1
            n -= num
        index += 1
    else:
        break
print (result)
"""

n = int(input())
fear_array = list(map(int, input().split()))
result = 0 # 총 그룹의 수
member = 0 # 현재 그룹에 포함된 모험가의 수

fear_array.sort()
for i in fear_array: # 공포도 낮은 것부터 하나씩 확인하며
    member += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if(i <= member): # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
        result += 1 # 그룹 수 1 증가
        member = 0 # 현재 그룹에 소속된 모험가의 수 초기화
print(result)