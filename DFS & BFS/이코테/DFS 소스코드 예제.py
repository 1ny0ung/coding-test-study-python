# DFS 메서드 정의
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
# 그래프는 시작 1 인 경우 많으므로 한 칸 비워 두고 시작
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드의 방문 여부 정보를 표현 (1차원 리스트트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)