'''
불의 이동: 인접한 4방향, 벽에는 불이 안 붙음
상근이의 이동: 인접한 4방향, 1초 소요. 
    벽 통과 X & 불이 옭겨진 칸 X & 불이 붙으려는 칸 X
    상근이가 있는 칸에 불이 옯겨옴과 동시에 다른 칸으로 이동할 수 있다.
    -> 불이 먼저 이동하여 상근이가 있는 자리에 불이 붙을 수 있음. 이때 상근이는 다른 칸으로 이동 가능

'.': 빈 공간
'#': 벽
'@': 상근이의 시작 위치
'*': 불

solution 
 - 불의 이동 BFS 구현
 - 상근이의 이동 BFS 구현
 - 공간에 가장자리 빈칸 추가하여 가장자리에 도달하면 탈출
 - 상근이가 모든 방향으로 이동한 경우, 불에 막힌 경우 IMPOSSIBLE
''' 
import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move_fire(q, map, n, m):
    len_ = len(q)
    for _ in range(len_):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 1 or nx > n or ny < 1 or ny > m:
                continue
            if map[nx][ny] not in ["#", "*"]:
                map[nx][ny] = "*"
                q.append([nx, ny])

def move_sg(q, map, n, m):
    len_ = len(q)
    for _ in range(len_):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == 0 or nx == n + 1 or ny == 0 or ny == m + 1:
                return True
            if nx < 0 or nx > (n + 1) or ny < 0 or ny > (m + 1):
                continue
            if map[nx][ny] == ".":
                map[nx][ny] = "@"
                q.append([nx, ny])

for test_case in range(T):
    fires = deque()
    pos = deque()
    m, n = map(int, input().split())
    graph = [['.'] * (m + 2)]
    for i in range(1, n + 1):
        row = input()
        graph.append(['.'])
        for j in range(m):
            if row[j] == "@":
                pos.append([i, j + 1])
            elif row[j] == "*":
                fires.append([i, j + 1])
            graph[i].append(row[j])
        graph[i].append('.')
    graph.append([['.'] * (m + 2)])

    escape = False
    answer = 0
    while not escape:
        if not pos:
            answer = "IMPOSSIBLE"
            break
        move_fire(fires, graph, n, m)
        escape = move_sg(pos, graph, n, m)
        answer += 1
    print(answer)

