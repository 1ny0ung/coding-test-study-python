### 백준 2751 번 수 정렬하기 2 ###
# 시간 복잡도 O(nlogn)을 가지는 정렬을 사용해야만 시간 초과하지 않는 문제
# 1. 파이썬 내장함수(sort) 사용
# 2. 퀵 정렬 사용
# 3. 병합 정렬 사용
# 4. 힙 정렬 사용

# 1. 파이썬 내장함수 사용한 풀이
import sys
# 입력 받을 숫자의 개수인 N
N = int(sys.stdin.readline().rstrip())
# 숫자들 저장할 리스트 N 
num = []
# N 개의 숫자들 num에 입력 받음
for i in range(N):
    num.append(int(sys.stdin.readline().rstrip()))
# 파이썬 내장 함수로 정렬
num.sort()
# 정렬된 숫자 형식대로 출력
for i in num:
    print(i)

'''
# 2-1. 퀵 정렬 사용 -> 메모리 초과! 
import sys

# 퀵 정렬 함수 
def quick_sort(array):
    if(len(array) <= 1):
        return array
    pivot = array[0]
    tail = array[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

# 입력 받을 숫자의 개수인 N
N = int(sys.stdin.readline().rstrip())
# 숫자들 저장할 리스트 N 
num = []
# N 개의 숫자들 num에 입력 받음
for i in range(N):
    num.append(int(sys.stdin.readline().rstrip()))

# 퀵 정렬 함수로 정렬
num = quick_sort(num)
# 정렬된 숫자 형식대로 출력
for i in num:
    print(i)
'''

'''
# 2-2. 퀵 정렬 정석대로 사용 -> 파이썬이 정한 재귀 깊이 초과! 
# 메모리 초과 방지하기 위해 안에서 리스트 선언 하지 않는 방식으로 구현
import sys

# 퀵 정렬 함수 
def quick_sort(array, start, end):
    if(start >= end):
        return
    pivot = start
    left = start + 1
    right = end

    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

    # 입력 받을 숫자의 개수인 N
N = int(sys.stdin.readline().rstrip())
# 숫자들 저장할 리스트 N 
num = []
# N 개의 숫자들 num에 입력 받음
for i in range(N):
    num.append(int(sys.stdin.readline().rstrip()))

# 퀵 정렬 수행
quick_sort(num, 0, N-1)

# 정렬된 숫자 형식대로 출력
for i in num:
    print(i)
'''