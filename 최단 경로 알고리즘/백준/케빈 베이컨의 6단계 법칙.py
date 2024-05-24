import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

graph = [[] for i in range(N+1)]
result = []
distance = [[INF] * (N+1) for i in range(N+1)]

for i in range(0, M):
    A, B = map(int, input().split())
    graph[A].append((B, 1))
    graph[B].append((A, 1))

def dijkstra(start): 
    q = []
    heapq.heappush(q, (0, start))
    distance[start][start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if(distance[start][now] < dist):
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[start][i[0]]:
                distance[start][i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

for i in range(1, N+1):
    temp = 0
    dijkstra(i)
    for j in range(1, N+1):
        temp += distance[i][j]
    result.append(temp)
print(result.index(min(result))+1)

