### 2606 번 바이러스 ###
### BFS 알고리즘 사용한 풀이 ###

import sys 
from collections import deque

# BFS 알고리즘 관련 처리하는 함수
# 시작 노드를 매개 변수로 받아 
# 아직 방문한 적 없는 연결된 노드에 방문할 때마다 count 1 씩 올림
# count 반환
def warm_bfs(start):
    count = 0
    queue = deque([start])
    visited[start] = True

    while queue:
        s = queue.popleft()
        virus_list = computers[s]
        for i in virus_list:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    return count

# 노드의 개수, 간선 개수 입력 받음
num = int(sys.stdin.readline().rstrip())
connections = int(sys.stdin.readline().rstrip())
# 노드별 연결 노드 저장할 리스트의 리스트 선언
# 이때 0 번은 비워 둠
computers = [[] for i in range(num+1)]

# 간선의 개수만큼 반복문 돌며 computers[간선 이루는 노드]에 다른 노드 추가
for i in range(connections):
    num_a, num_b = map(int, sys.stdin.readline().rstrip().split())
    computers[num_a].append(num_b)
    computers[num_b].append(num_a)

# 노드 별 방문 여부 저장할 리스트 visited 선언
visited = [False] * (num+1)
# 1 번 노드를 시작으로 BFS 처리 -> 결과 출력
print(warm_bfs(1))

