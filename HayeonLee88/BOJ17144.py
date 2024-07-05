import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

r, c, t = map(int, input().split())

graph = [] # 방의 정보를 담는 그래프
dust = deque() # 먼지들의 위치
vacuum = [] # [0]: 위, [1]: 아래

for i in range(r):
    row = list(map(int, input().split()))
    for j in range(c):
        if row[j] == 0:
            continue
        elif row[j] > 0:
            dust.append([row[j], i, j])
        else:
            vacuum.append([i, j])
    graph.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

move = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]} # default: 위, x축 * -1: 아래

def cleaning(x, y, pos):
    global graph, r, c
    x_ = x - 1 * pos
    y_ = y
    dir = 0

    while True:
        # 먼지의 이동
        if graph[x_][y_] > 0:
            mx = x_ + move[dir][0] * pos * -1
            my = y_ + move[dir][1] * -1
            if [mx, my] != [x, y]:
                graph[mx][my] = graph[x_][y_]
            graph[x_][y_] = 0
        # 바람의 이동
        nx = x_ + move[dir][0] * pos
        ny = y_ + move[dir][1]
        if [nx, ny] == [x, y]:
            break
        if pos == 1:
            if nx < 0  or nx > x or ny < 0  or ny >= c:
                dir = (dir + 1) % 4
                continue
        else:
            if nx < x  or nx >= r or ny < 0  or ny >= c:
                dir = (dir + 1) % 4
                continue
        x_ = nx
        y_ = ny

for _ in range(t):
    len_ = len(dust)
    for i in range(len_):
        num, x, y = dust.popleft()
        d = num // 5
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if graph[nx][ny] >= 0:
                graph[nx][ny] += d
                graph[x][y] -= d

    cleaning(vacuum[0][0], vacuum[0][1], 1)
    cleaning(vacuum[1][0], vacuum[1][1], -1)

    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                dust.append([graph[i][j], i, j])

answer = 2
for row in graph:
    answer += sum(row)

print(answer)