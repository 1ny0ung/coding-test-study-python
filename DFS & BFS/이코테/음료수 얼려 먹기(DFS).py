import sys

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def DFS_ice(start_x, start_y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if(start_x < 0 or start_x >= M or start_y < 0 or start_y >= N):
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if(ice[start_y][start_x] == 0):
        # 해당 노드 방문 처리
        ice[start_y][start_x] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        DFS_ice(start_x - 1, start_y)
        DFS_ice(start_x + 1, start_y)
        DFS_ice(start_x, start_y - 1)
        DFS_ice(start_x, start_y + 1)
        return True
    return False

# N, M을 공백을 기준으로 구분하여 입력 받기
N, M = map(int, sys.stdin.readline().rstrip().split())

# 2 차원 리스트의 맵 정보 입력 받기
ice = []
for n in range(N):
    ice.append(list(map(int, sys.stdin.readline().rstrip())))

# 모든 노드(위치)에 대해 음료수 채우기
result = 0
for n in range(N):
    for m in range(M):
        if DFS_ice(m, n) == True:
            result += 1
# 정답 출력
print(result)