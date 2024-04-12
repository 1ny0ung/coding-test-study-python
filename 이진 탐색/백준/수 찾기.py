# 백준 #1920: 수 찾기

import sys
# 이진 탐색 라이브러리 불러옴
from bisect import bisect_left
input = sys.stdin.readline

# N 개의 정수 입력 받음
N = int(input().rstrip())
list_a = list(map(int, input().rstrip().split()))
# M 개의 정수 입력 받음
M = int(input().rstrip())
list_b = list(map(int, input().rstrip().split()))

# 이진 탐색 대상인 list_a 오름차순 정렬
list_a.sort()

# bisect_left 하면 list_b의 원소보다 작은 값들만 왼쪽에 두고, 그 다음 index를 반환하므로
# list_a에서 bisect_left 인덱스가 가리키는 값이 list_b의 원소 값과 같다면 서로 일치하는 값이 존재하는 것이다.
for b in list_b:
    index = bisect_left(list_a, b)
    # list_b의 원소가 list_a의 최댓값보다 큰 경우 N을 반환하므로 그대로 list_a[index] 처리하면 인덱스 초과 -> 조건문 사용
    # 이 경우 일치값이 없는 것이므로 0 출력
    if index >= N: 
        print(0)
    elif(b == list_a[index]):
        print(1)
    else:
        print(0)