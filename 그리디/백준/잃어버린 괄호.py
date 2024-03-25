expression = input().split('-')

for i in range(0, len(expression)):
    sub = map(int,expression[i].split('+'))
    plus_result = sum(sub)
    expression[i] = plus_result

result = expression[0] - sum(expression[1:])
print(result)
