import sys
import copy
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
# 시계 방향으로 90도씩 회전
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph = []
cctvs = []

answer = 64
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j, x in enumerate(graph[i]):
        if x in [1, 2, 3, 4, 5]:
            cctvs.append((x, [i, j]))

def cctv(x, y, i, graph):
    i = i % 4
    while True:
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        if graph[nx][ny] == 6:
            break
        elif graph[nx][ny] == 0:
            graph[nx][ny] = -1
        x = nx
        y = ny

def dfs(i, graph):
    global answer
    if i == len(cctvs):
        cnt = 0
        for row in graph:
            cnt += row.count(0)
        answer = min(answer, cnt)
        return

    num = cctvs[i][0]
    x, y = cctvs[i][1][0], cctvs[i][1][1]
    for dir in range(4):
        tmp = copy.deepcopy(graph)
        if num == 1:
            cctv(x, y, dir, tmp)
        elif num == 2:
            cctv(x, y, dir, tmp)
            cctv(x, y, dir + 2, tmp)
        elif num == 3:
            cctv(x, y, dir, tmp)
            cctv(x, y, dir + 1, tmp)
        elif num == 4:
            cctv(x, y, dir, tmp)
            cctv(x, y, dir + 1, tmp)
            cctv(x, y, dir + 2, tmp)
        elif num == 5:
            cctv(x, y, dir, tmp)
            cctv(x, y, dir + 1, tmp)
            cctv(x, y, dir + 2, tmp)
            cctv(x, y, dir + 3, tmp)
        
        dfs(i + 1, tmp) # 다음 cctv 탐색
        
dfs(0, graph)
print(answer)