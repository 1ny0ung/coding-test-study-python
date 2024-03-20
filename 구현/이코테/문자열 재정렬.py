"""
input_str = input()
num = 0
alpha_array = list()
for i in range(len(input_str)):
    if(input_str[i].isdigit()):
        num += int(input_str[i])
    else:
        alpha_array.append(input_str[i])
alpha_array.sort()
print(''.join(alpha_array) + str(num))
"""
data = input()
result = []
value = 0

for x in data:
    if(x.isalpha()):
        result.append(x)
    else:
        value += int(x)

result.sort()
if(value != 0):
    result.append(str(value))

print(''.join(result))