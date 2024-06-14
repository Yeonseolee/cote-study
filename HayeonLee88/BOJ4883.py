'''
2 이상인 N행과 3열로 이루어진 삼각 그래프
1행 2열에서 N행 2열까지 가는 최단 거리를 구하기
경로의 비용: 지나간 정점의 비용의 합

2 ≤ N ≤ 100,000

이동 방향
1열
1. 같은 행 다음 열
2. 다음 행 같은 열
3. 다음 행 다음 열
2열
1. 같은 행 다음 열
2. 다음 행 같은 열
3. 다음 행 이전 열
4. 다음 행 다음 열
3열
1. 같은 행 다음 열
2. 다음 행 같은 열
3. 다음 행 이전 열

풀이
- DP 테이블 생성
- 각 행과 열에서의 최소 비용 구하기
    - i행 1열: i-1행 1열, i-1행 2열 중 최소
    - i행 2열: i-1행 1열, i-1행 2열, i-1행 3열, i행 1열 중 최소
    - i행 3열: i-1행 2열, i-1행 3열, i행 2열
'''
import sys

INF = int(1e9)

def DP(graph, n):
    dp = [[INF] * 3 for _ in range(n)]
    dp[0] = [INF, graph[0][1], graph[0][1] + graph[0][2]]
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + graph[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i][0]) + graph[i][1]
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][2], dp[i][1]) + graph[i][2]
    return dp[-1][1]

input = lambda: sys.stdin.readline().rstrip()

k = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    print(f'{k}. {DP(graph, n)}')
    k += 1