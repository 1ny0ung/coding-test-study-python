# N, K를 공백을 기준으로 구분해서 입력 받기
N, K = map(int, input().split())
count = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (N // K) * K
    count += N - target
    N = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if N < K:
        break
    # K로 나누기
    N //= K
    count +=1

# 마지막으로 남은 수에 대하여 1씩 빼기    
count += N - 1
print(count)