from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split()) 
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상하좌우에 익지 않은 토마토(0)가 있으면 1을 더해 몇 번째인지 세줌
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny)) # 새로운 토마토 위치 추가
                
bfs()

# bfs 종료 후
day = 0
for row in graph:
    for i in row:
        if i == 0:  
            print(-1)
            exit()
    else:
        day = max(day, max(row)) 

print(day-1)
