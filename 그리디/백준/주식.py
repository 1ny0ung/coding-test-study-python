import sys

test_case = int(sys.stdin.readline().rstrip())

for turn in range(0, test_case):
    n = int(sys.stdin.readline().rstrip())
    price: list[int] = [None for i in range(0, n)]
    price = list(map(int, sys.stdin.readline().rstrip().split()))

    ### 시간 초과 이슈 - 뒤에서부터 조회해 시간 복잡도 낮춰야 함 ###
    ### 증가하는 동안 max 계속 갱신하다 max보다 낮아지면 차익을 냄 ###
    ### max보다 더 높은 값 나오면 그 가격에 팔면 감소 그래프 - 손해가 나서 팔 수 없으므로 max 갱신 ###
    max_price = 0
    profit = 0

    for i in range(n-1, -1, -1):
        if(price[i] > max_price):
            max_price = price[i]
        else:
            profit += max_price - price[i]

    print(profit)

