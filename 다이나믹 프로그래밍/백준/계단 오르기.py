# 2579 번: 계단 오르기

import sys
input = sys.stdin.readline

n = int(input().rstrip())
# d[n]에 계단의 개수 n만큼 오르는 동안의 점수의 최댓값을 저장
# => n만큼 만드니 index error 발생해 301로 변경
d = [0] * 301

# 계단마다의 점수를 저장 
# => n만큼 만드니 index error 발생해 301로 변경
score = [0] * 301
for i in range(1, n+1):
    score[i] = int(input().rstrip())

# 점화식
# 계단을 오르는 방법은 1 칸을 오르거나 2 칸을 오르거나임.
# n 개의 계단을 오르는 동안의 점수의 최댓값은 d[n-1]에서 1 칸 올랐을 때의 점수와 d[n-2]에서 2 칸을 한 번에 올랐을 때의 점수를 비교한 것 중 큰 값.
# 단, 3 번 연속 1 칸씩만 오르는 경우 피하기 위해 d[n-1]에서 1 칸 오르는 경우 d[n-3]에서 d[n-1]로 온 상태여야 함 
# 따라서 d(n) = {d(n-3) + n-1 번째 계단의 점수와 d(n-2) 계단의 점수 비교해 더 큰 값} + n 번째 칸의 점수

# 초기값
d[0] = 0
d[1] = score[1]
d[2] = score[1] + score[2]
d[3] = max(score[2], d[1]) + score[3]

for i in range(4, n+1):
    d[i] = max(d[i-3] + score[i-1], d[i-2]) + score[i]

print(d[n])

