import sys
input = sys.stdin.readline
import copy

def function(N, array):
    dp = copy.deepcopy(array)
    
    dp[0][2] = array[0][1] + array[0][2]
    dp[1][0] = dp[0][1] + array[1][0]
    dp[1][1] = dp[0][1] + array[1][1]
    #dp[1][1] = min(dp[0][1] + array[1][1], dp[1][0] + array[1][1], dp[0][2] + array[1][1])
    dp[1][2] = dp[0][1] + array[1][2]
    #dp[1][2] = min(dp[0][1] + array[1][2], dp[0][2] + array[1][2], dp[1][1] + array[1][2])
    
    if N == 2:
        return dp[1][1]

    i = 2
    
    while i < N:
        #dp[i][0] = min(dp[i-1][0] + array[i][0], dp[i-1][1] + array[i][0])
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + array[i][0]
        #dp[i][1] = min(dp[i-1][1] + array[i][1], dp[i-1][0] + array[i][1], dp[i][0] + array[i][1], dp[i-1][2] + array[i][1])
        dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + array[i][1]
        #dp[i][2] = min(dp[i-1][2] + array[i][2], dp[i-1][1] + array[i][2], dp[i][1] + array[i][2])
        dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + array[i][2]
        i += 1
    return dp[N-1][1]


idx = 0

while True:
    idx += 1
    N = int(input())
    if N == 0:
        break
    
    array = []
    for _ in range(N):
        array.append(list(map(int,input().split())))
    result = function(N, array)
    print(f'{idx}. {result}')