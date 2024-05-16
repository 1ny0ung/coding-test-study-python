import sys
input = sys.stdin.readline

s = input().rstrip()
def solution(s):
    answer = 0
    for i in range(0, len(s)):
        for j in range(len(s)-1, -1, -1):
            if(s[i:j] == s[j:i:-1]):
                answer = (j-i+1) if(j-i+1 > answer) else answer
                
    return answer

print(solution(s))