import sys
input = sys.stdin.readline

N = int(input())
routes = []
for i in range(N):
    [a, b] = map(int, input().split())
    routes.append([a, b])

def solution(routes):
    routes.sort()
    camera = []
    camera.append(routes[0])
    for route in routes:
        length = len(camera)
        for i in range(length):
            if (route[1] < camera[i][0] or route[0] > camera[i][1]):
                if i == length - 1:
                    camera.append(route) 
                continue
            else: 
                camera[i][0] = route[0] if(camera[i][0] < route[0]) else camera[i][0]
                camera[i][1] = route[1] if(camera[i][1] > route[1]) else camera[i][1]
            break
    answer = len(camera) 
    return answer
print(solution(routes))