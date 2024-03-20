"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
dx = [-1, -1, 1, 1, -2, -2, 2, 2]
dy = [-2, 2, -2, 2, -1, 1, -1, 1]

pos = str(input())
result = 0 

x = int(pos[1])
y = alphabet.index(pos[0]) + 1

for i in range(8):
    nx = x + dx[i]
    ny = x + dy[i]
    if(nx > 0 and nx < 9 and ny > 0 and ny < 9):
        result += 1
print(result)
"""
input_data = input()
row = int(input_data[1])
column = ord(input_data[0]) - ord('a') + 1

steps = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if(next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8):
        result += 1

print(result)