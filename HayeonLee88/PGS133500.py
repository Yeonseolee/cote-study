import sys
sys.setrecursionlimit(100000)

def solution(n, lighthouse):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in lighthouse:
        graph[u].append(v)
        graph[v].append(u)
    
    dp = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    def dfs(i):
        visited[i] = True
        dp[i][0] = 0  # i번째 등대를 안 켰을 때 켜야될 인접한 등대의 최소 개수
        dp[i][1] = 1  # i번째 등대를 켰을 때 켜야 될 인접한 등재의 최소 개수 + 1(i번째 등대)
        for x in graph[i]:
            if not visited[x]:
                dfs(x) # 인접 등대 탐색
                # i번째 등대가 꺼져있기 때문에 인접한 등대 x가 켜졌을 때를 더한다.
                dp[i][0] += dp[x][1] # 등대 x를 켰을 때 켜야될 x의 인접 등대 최소 개수 더하기
                # i번째 등대가 켜있기 때문에 인접한 등대 x가 켜졌을 때 또는 꺼졌을 때의 최소값을 더한다.
                dp[i][1] += min(dp[x][0], dp[x][1]) # 등대 x를 껐을 때 또는 켰을 때의 켜야될 x의 인접 등대 최소 개수 중 최소값 더하기
    
    dfs(1)

    return min(dp[1][0], dp[1][1])