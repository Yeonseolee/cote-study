n = int(input())

dp = [0] * (n+1)

# dp[i] = i를 만들기 위해 필요한 최소 연산횟수
for i in range(2, n+1):
    # 1을 빼기
    dp[i] = dp[i-1] + 1

    # 2로 나눠진 것 전에서 더하기 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

    # 3으로 나눠지면 3으로 나눠진 전 것에서 더하기 1
    # 현재 거랑 더 작은거 비교하기
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])
        
# 역으로 돌면서 1차이가 나면 돌아가기
while n > 1:
    print(n, end=" ")
    if dp[n] == dp[n-1] + 1:
        n -= 1

    elif n % 2 == 0 and dp[n] == dp[n // 2] + 1:
        n = n // 2
    
    elif n % 3 == 0 and dp[n] == dp[n//3] + 1:
        n = n//3

print(n)