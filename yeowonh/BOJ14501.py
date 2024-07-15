"""
DP 문제

백준이가 얻을 수 있는 최대 수익
dp[i] = i번째 날부터 마지막날까지 낼 수 있는 최대의 이익
최대값 = 현재 상담일자의 이윤 + 현재 상담을 마친 일자로부터의 최대 이윤

예시 1. (편의상 인덱스 1부터)
dp[7] -> i + T_i > N = 0
dp[6] -> i + T_i > N = 0
dp[5] -> i + T_i <= N
-> dp[5] = p[5]

dp[4] -> i + T_i <= N
p[4] + dp[i + T_i], max_value

dp[3] -> i + T_i <= N
p[3] + dp[i + T_i], max_value

...
"""
N = int(input())

# 인덱스 1부터 시작하기 위해
dp_list = [0] * (N+1) 
t_list = []; p_list = []

for _ in range(N):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

for i in range(N-1, -1, -1):
    # 상담 불가할 경우 : 전날 거 그대로
    if i + t_list[i] > N:
        dp_list[i] = dp_list[i+1]
    
    # 상담 가능할 경우
    # 전날까지의 최대값  VS 현재 상담 일자의 이윤 + 현재 상담을 마친 일자부터의 최대 이윤
    else:
        dp_list[i] = max(dp_list[i+1], p_list[i] + dp_list[i + t_list[i]])

print(dp_list[0])
