# 1793 번: 파일링 문제 풀이

import sys

d = [0] * 251
input = sys.stdin.readline

while(True):
    try:
        n = int(input().rstrip())
        
        # 점화식
        # d(n) = d(n-1)에서 가로 1 끼워 넣기 + d(n-2)에서 가로 2 끼워 넣기
        # 주의! d(n-2)에서 세로 2개로 끼워넣는 건 d(n-1)에서 세로 1개 넣는 케이스에서 이미 했으므로 제외

        d[0] = 1
        d[1] = 1
        d[2] = 3

        for i in range (3, n+1):
            d[i] = d[i-1] + 2*d[i-2]
        
        print(d[n])
    except:
        break
    