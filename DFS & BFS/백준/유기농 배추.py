# 1012 번 유기농 배추
# DFS를 활용해 풀이

import sys

# 상하좌우 좌표 저장
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# DFS를 활용해 탐색이 끝나면 하나의 배추 구역 -> 1 return
def cabbage_dfs(start_x, start_y):
    visited[start_y][start_x] = True

    for d in dir:
        pos_x = start_x + d[0]
        pos_y = start_y + d[1]
        # 인접 구역 x, y가 밭 범위에 있고
        if (0 <= pos_x < M and 0 <= pos_y < N):
            # 인접 구역이 방문된 적 없고 배추가 심겨져 있을 때(1) => 함수 다시 호출해 탐색 이어감
            if (visited[pos_y][pos_x] == False and farm[pos_y][pos_x] == 1):
                cabbage_dfs(pos_x, pos_y)
    return 1        

# 테스트 케이스 개수 입력 받음
T = int(sys.stdin.readline().rstrip())

# 테스트 케이스 개수만큼 반복
# 이때 변수들 초기화 될 수 있도록 주의!
for __ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    # m x k 크기 2 차원 리스트 farm 선언 (초기값 0)
    farm = [[0] * M for __ in range(N)]

    # K 줄의 입력 값 읽어 들여 배추 위치에 1 표시    
    for i in range(K):
        dx, dy = map(int, sys.stdin.readline().rstrip().split())
        farm[dy][dx] = 1

    # 방문 여부 저장하는 배열 visited, 필요한 지렁이 개수 저장하는 변수 count
    visited = [[False] * M for __ in range(N)]
    count = 0

    for y in range(N):
        for x in range(M):
            # 배추가 심겨 있고 방문된 적 없는 구역일 때
            # 새로운 배추 구역이므로 함수 호출 -> 탐색 끝나면 결과에 +1
            if (farm[y][x] == 1 and visited[y][x] == False):
                count += cabbage_dfs(x, y)

    print(count)