'''
N: 물건 개수
(W, V): 물건의 무게, 가치
K: 담을 수 있는 최대 무게

[N][K] 사이즈인 이차원 배열을 사용한다.

'''
import sys
input = lambda:sys.stdin.readline().rstrip()

n, k = map(int, input().split())
stuff = [[]]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for _ in range(n):
    stuff.append(list(map(int, input().split())))

for i in range(1, n + 1):
    w, v = stuff[i]
    for j in range(1, k + 1):
        if w <= j:
            dp[i][j] = max(dp[i - 1][j], (dp[i - 1][j - w] + v))
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])
