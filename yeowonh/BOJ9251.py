import sys
def solution(a, b):
    dp = [[0]* (len(b)) for _ in range(len(a))]

    for i in range(1, len(a)):
        for j in range(1, len(b)):
			      # 이전 LCS 길이에 1만큼 더해주면 됨
            if a[i] == b[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[-1][-1]


a = ' ' + sys.stdin.readline().rstrip()
b = ' ' + sys.stdin.readline().rstrip()

print(solution(a, b))