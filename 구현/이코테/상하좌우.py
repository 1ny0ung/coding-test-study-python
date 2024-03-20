"""
# 여행자의 좌표
traveler_X = 1
traveler_Y = 1

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 입력값 받아오기
N = int(input())
array_plan = list(input().split())

for i in range(len(array_plan)):
    if (array_plan[i] == "R") and (traveler_Y < N):
        traveler_Y += dy[0]
    elif (array_plan[i] == "L") and (traveler_Y > 1):
        traveler_Y += dy[1]
    elif (array_plan[i] == "D") and (traveler_X < N):
        traveler_X += dx[2]
    elif (array_plan[i] == "U") and (traveler_X > 1):
        traveler_X += dx[3]

print(traveler_X, traveler_Y)
"""

n = int(input())
plans = input().split()
x, y = 1, 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
move_types = ['R', 'L', 'D', 'U']

for plan in plans:
    for i in range(len(move_types)):
        if(plan == move_types[i]):
            nx = x + dx[i]
            ny = y + dy[i]
            break
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)