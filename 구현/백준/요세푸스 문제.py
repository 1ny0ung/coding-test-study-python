### 1158 번 요세푸스 문제 ###

import sys
input = sys.stdin.readline().rstrip()
# N, K 입력 받기
N, K = map(int, input.split())
# 1~N까지 숫자 저장하는 배열 생성
array = [x for x in range(1, N+1)]
# 결과값 저장할 문자열 result
result = "<"
# 마지막으로 사람 제거한 index 저장할 변수 index
index = 0
# 현재 array의 max index 저장할 변수 max
max = N-1
# N 번 동안, 사람이 모두 제거될 때까지 반복
for x in range(N):
    # 다음에 제거할 사람의 인덱스 
    index += K - 1
    # array의 max index 초과한 경우 0 번째 사람부터 다시 카운트
    # 이때 남은 사람이 K보다 작아지는 경우 한 번 수행으로는 max index 초과하게 되는 경우 발생 (ex. 남은 사람 2 명인데 k = 4)
    # 그래서 반복문으로 조건문 만족할 때까지 반복(원형 배열 -> 다시 0 번째 사람부터 카운트 하는 것 가능)
    while(index > max):
        index -= max + 1
    # 빼야 할 사람 형식에 맞춰 result에 추가
    result += str(array.pop(index)) + ", "
    # 사람 1 명 줄었으므로 max - 1
    max -= 1
# 결과 출력
result = result[:-2] + ">"
print(result)