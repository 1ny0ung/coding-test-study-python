import sys

'''
### 내 정답 코드 ###
N, K = map(int, sys.stdin.readline().rstrip().split())
array_A = list(map(int, sys.stdin.readline().rstrip().split()))
array_B = list(map(int, sys.stdin.readline().rstrip().split()))

array_A = sorted(array_A)
array_B = sorted(array_B)

for i in range(K):
    if(array_A[i] < array_B[N-1-i]):
        array_A[i] = array_B[N-1-i]
    else:
        break

print(sum(array_A))
'''

### 정답 코드 예제 ###
n, k = map(int, input().split()) # n과 k를 입력 받기
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력 받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력 받기

a.sort() # 배열 A는 오름차순 정렬
b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행 -> 내 코드와의 차이점

for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if(a[i] < b[i]): 
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    # A의 원소가 B의 원소보다 크거나 같으면 반복문 탈출
    else:
        break

print(sum(a)) # 배열 A의 모든 원소들의 합 출력