# 백준 #7795: 먹을 것인가 먹힐 것인가

import sys
# 이진 탐색 라이브러리 불러옴
# 이때 A는 자신보다 작은 B의 원소들을 세어야 하므로 
# B의 원소가 자신의 값보다 같거나 커지면 바로 탐색 중단하고 인덱스를 반환해야 한다.
# 따라서 A가 삽입될 수 있는 가장 왼쪽 인덱스를 반환하는 bisect_left 사용
from bisect import bisect_left
input = sys.stdin.readline

# 테스트 케이스 개수 입력 받음
T = int(input().rstrip())
# 테스트 케이스만큼 반복
for __ in range(T):
    # A와 B의 원소의 개수인 N, M 입력 받음 
    N, M = map(int, input().rstrip().split())
    # A와 B의 배열 입력 받음
    list_a = list(map(int, input().rstrip().split()))
    list_b = list(map(int, input().rstrip().split()))

    # 이진 탐색을 위해 오름차순으로 정렬
    list_a.sort()
    list_b.sort()

    # A의 원소가 B의 원소보다 클 때의 경우의 수를 저장할 변수
    count = 0
    # 모든 A의 원소마다 이진 탐색 실행
    for a in list_a:
        count += bisect_left(list_b, a)
    print(count)