# 백준 #4386 번: 별자리 만들기

import sys
import math
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if(parent[x] != x):
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 각 별의 위치 저장할 배열
stars = []

# 별의 개수 n 입력 받음
n = int(input())
for i in range(n):
    x, y = map(float, input().split())
    stars.append([x, y])

# 각 별의 부모 노드 저장할 배열
parent = [i for i in range(n)]

# 모든 별에 대해 서로 이어지는 간선 정보 생성
edges = []
for i in range(n):
    for j in range(i+1, n):
        dist_x = stars[i][0] - stars[j][0]
        dist_y = stars[i][1] - stars[j][1]
        cost = math.sqrt(dist_x**2 + dist_y**2)
        edges.append((cost, i, j))
edges.sort()

result = 0

# 간선을 하나씩 확인하며
for edge in edges:
     cost, a, b = edge
     if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)