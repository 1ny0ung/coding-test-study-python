### 백준 10814 번 나이순 정렬 ###

import sys

# 온라인 저지 회원의 수 입력 받기
N = int(sys.stdin.readline().rstrip())
# N 개의 리스트를 요소로 가지는 멤버 리스트 생성
member = [[] for __ in range(N)]

# 멤버 정보 N 번 입력 받음
for i in range(N):
    age, name = sys.stdin.readline().rstrip().split()
    member[i] = [int(age), name]

# 2 차원 배열의 정렬 사용 
# -> 각 리스트의 첫 번째 인덱스에 대해 오름차순 정렬, 
# 여기서 튜플로 x[1] 추가하는 경우 -> 동일 값인 경우 두 번째 인덱스에 대해 오름차순 정렬 진행
member.sort(key=lambda x: x[0])

for i in member:
    for j in i:
        print(j, end=' ')
    print()