### 백준 1446: 지름길 문제 풀이 ###
import sys
input = sys.stdin.readline
import heapq

# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9) 

# 지름길 개수와 목표 지점까지의 거리 N, D 입력 받음
N, D = map(int, input().split())
# 고속도로 1 KM 마다 노드가 있다고 가정 -> 각 노드는 자기 인덱스 +1 번 노드와 1 km 거리로 전부 연결
# 노드마다 연결된 간선 표시할 graph 
graph = [[] for i in range(D+1)]
# 0 번부터 D-1 번까지 1 km 더 간 지점과의 관계 graph에 반영
for i in range(0, D):
    graph[i].append((i+1, 1))
# 0km 지점부터 인덱스 지점까지의 거리 나타내 줄 distance INF로 초기화
distance = [INF] * (D+1)

# 지름길 입력 받아 graph에 반영
for i in range(N):
    start, arrive, dist = map(int, input().split())
    if (arrive > D):
        continue
    graph[start].append((arrive, dist))

# 다익스트라 알고리즘 함수
def dijkstra(start):
    # 우선순위 큐 리스트 q
    q = [] 
    # 시작 지점을 q에 넣고 distance도 0으로 설정
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # q가 빌 때까지 반복 
    while q:
        # q에서 현재 최단거리 노드의 거리와 인덱스 뽑음
        dist, now = heapq.heappop(q)
        # 만약 이미 방문 처리된 노드라면 넘어감 
        if distance[now] < dist:
            continue
        # 아직 방문하지 않은 노드의 경우 인접 노드들에 관해 현재 노드를 거쳐 인접 노드로 가는 거리 계산
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                # 계산한 거리와 원래 인접 노드까지의 최단 거리 비교 후 현재 노드 거치는 쪽 값이 더 작으면 distance 갱신
                distance[i[0]] = cost
                # 힙에도 정보 넣어 줌
                heapq.heappush(q, (cost, i[0]))

# 0 km 지점에서 다익스트라 시작
dijkstra(0)
# 고속도로 끝 지점까지의 최단 거리 출력
print(distance[D])
