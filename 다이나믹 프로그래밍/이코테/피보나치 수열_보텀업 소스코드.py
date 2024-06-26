### 피보나치 수열: 보텀업 다이나믹 프로그래밍 소스 코드 ###
# 작은 문제들을 먼저 해결 -> 해결해 두었던 작은 문제를 조합해서 큰 문제 풀어나감.

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
# 100 개의 원소를 가지는 리스트 -> 0~99의 인덱스를 가지게 됨 -> 예제에서 fibo(99) 구하므로!
# 각 인덱스에 해당하는 결과를 0으로 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
# 보텀업 방식에서는 재귀함수 대신 반복문이 사용됨 -> 종료 조건 대신 점화식에서의 시작항에 대한 값들을 DP 테이블에 초기화
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현(보텀업 방식)
# 점화식 그대로 기입하여 반복문 수행 -> 3 번째부터 99 번째까지 차례대로 모든 피보나치 수 구함
for i in range(3, n+1):
    d[i] = d[i-2] + d[i-1]

print(d[n])