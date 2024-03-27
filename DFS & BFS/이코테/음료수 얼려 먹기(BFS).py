import sys
from collections import deque

dir = [(-1, 0),(1, 0),(0, -1),(0, 1)]

def ice_bfs(start_n, start_m):
    visited[start_n][start_m] = True
    queue = deque([(start_n, start_m)])
    if(ice_frame[start_n][start_m] == 1):
        return False
    
    while(queue):
        x, y = queue.popleft()
        for i in range(0, 4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if ((0 <= nx < n) and (0 <= ny < m) and (ice_frame[nx][ny] == 0) and (visited[nx][ny] == False)):
                visited[nx][ny] = True
                queue.append((nx, ny))
    return True

n, m = map(int, sys.stdin.readline().rstrip().split())
ice_frame = list()
for i in range(0, n):
    ice_frame.append(list(map(int, sys.stdin.readline().rstrip())))

count = 0
visited = [[False] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if not (visited[i][j]):
            if(ice_bfs(i, j)):
                count += 1

print(count)