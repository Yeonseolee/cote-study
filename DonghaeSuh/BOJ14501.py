N=int(input())
consultings = [list(map(int,input().split())) for _ in range(N)]

dp = [0]*(N+1)

for i in range(N):
    for j in range(i+consultings[i][0], N+1):
        if dp[j] < dp[i] + consultings[i][1]:
            dp[j] = dp[i] + consultings[i][1]
            
print(dp[-1])
