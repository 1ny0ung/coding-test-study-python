import sys
input = sys.stdin.readline
N = int(input())
array = [x for x in input().split()]
commands = []
for i in range(N):
    commands.append(list(map(int, input().split())))
def find_k(commands):
    i = commands[0] - 1
    j = commands[1] - 1
    k = commands[2]
    cut = array[i:j+1]
    cut.sort()
    return cut[k-1]
result = []
for i in range(N):
    result.append(find_k(commands[i]))
print(result)