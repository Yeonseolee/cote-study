#  점화식을 못 구하겠어서 답지 봄 : https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence#%EC%B5%9C%EC%9E%A5-%EA%B3%B5%ED%86%B5-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4longest-common-subsequence-%EA%B8%B8%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0

import sys

input = lambda : sys.stdin.readline().rstrip()
s1, s2 = [input() for _ in range(2)]

dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]

# dp의 idx 0에는 초기값(마진값)을 위해 0으로 설정했으므로, 문자열도 맞춰줄 것.
s1, s2 = ' '+s1, ' '+s2

# i 는 s2, j는 s1
for i in range(len(dp)):
    for j in range(len(dp[0])):
        if i == 0 or j == 0: # 초기값 설정
            continue
        if s2[i] == s1[j]: # 같은 문자열이면 대각선 왼쪽 위 방향 + 1
            dp[i][j] = dp[i-1][j-1] + 1
        else: # 다른 문자열이면 상, 좌 중 큰 값 (연속성 부여)
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])

    
    
