# 1260 번 DFS와 BFS

import sys
from collections import deque

# BFS 실행 함수
def BFS(start):
    visited[start] = True
    queue = deque([start])

    while(queue):
        s = queue.popleft()
        print(s, end=' ')
        v_list = graph[s]
        for v in v_list:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

# DFS 실행 함수
def DFS(start):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            DFS(i)
    
# N, M, V입력 받아 옴
N, M, V = map(int, sys.stdin.readline().rstrip().split())
# N+1 개의 리스트를 가지는 리스트 선언
graph = [[] for i in range(N+1)]

# 간선 개수만큼 반복문으로 graph에 각각의 연결 관계 넣어 줌
for __ in range(M):
    num_a, num_b = map(int, sys.stdin.readline().rstrip().split())
    graph[num_a].append(num_b)
    graph[num_b].append(num_a)

# graph에 저장한 인접 지점을 숫자 순서대로 정렬
# 문제에서 방문 가능한 인접 노드들이 여러 개면 숫자가 작은 것부터 방문하라고 했으므로! 
for num in graph:
    num.sort()

# 방문 여부 나타내는 visited 초기화해 가며
# DFS와 BFS 함수 차례로 실행
visited = [False] * (N+1)
DFS(V)
print()
visited = [False] * (N+1)
BFS(V) 

