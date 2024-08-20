'''
5:19 ~ 5:29
'''
import sys

sys.setrecursionlimit(100000)
input = lambda:sys.stdin.readline().rstrip()

T = int(input())
n, m, k = 0, 0, 0
graph = []
def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    else:
        if graph[x][y] == 1:
            graph[x][y] = 0
            DFS(x + 1, y)
            DFS(x, y + 1)
            DFS(x - 1, y)
            DFS(x, y - 1)
            return True
    return False


for test_case in range(T):
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    for i in range(n):
        for j in range(m):
            if DFS(i, j):
                cnt += 1
    print(cnt)
