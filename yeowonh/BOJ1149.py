def solution(N):
    cost = []

    for _ in range(N):
        cost.append(list(map(int, input().split())))


    for i in range(1, N):
        # 다음 입력값이 R, G, B일 때 세가지로 나누어 계산
        # R일 때
        cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
        # G일 때
        cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
        # B일 때
        cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]
        
        
    return min(cost[N-1][0], cost[N-1][1], cost[N-1][2])

N = int(input())
print(solution(N))