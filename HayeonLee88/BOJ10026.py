import sys
from collections import deque
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
graph = []
visited = [[False] * n  for _ in range(n)]
for i in range(n):
    graph.append(input())

move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

def BFS(x, y):
    q = deque()
    q.append((x, y))
    color = graph[x][y]
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + move_x[i]
            ny = y + move_y[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and graph[nx][ny] == color:
                visited[nx][ny] = True
                q.append((nx, ny))
                
for k in range(2):
    cnt = 0
    visited = [[False] * n  for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                BFS(i, j)
                cnt += 1
        graph[i] = graph[i].replace('G', 'R')
    print(cnt, end=' ')