import sys
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

back = {0:[1, 0], 1: [0, -1], 2: [-1, 0], 3: [0, 1]} # 후진 방향
forward = {0:[-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]} # 전진 방향

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

stop = False # 청소를 멈추기 위한 bool 변수
answer = 0

while not stop:
    if graph[r][c] == 0:
        graph[r][c] = -1
        answer += 1

    check = False 
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if graph[nx][ny] == 0: # 청소되지 않은 빈 칸이 있다면
            check = True
            d = (d - 1) % 4 # 반시계 90도 회전
            fx, fy = forward[d]
            if graph[r + fx][c + fy] == 0: # 앞이 청소되지 않은 빈 칸이면 전진
                r = r + fx
                c = c + fy
                break
    if not check: # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        bx, by = back[d]
        nx = r + bx
        ny = c + by
        if graph[nx][ny] == 1: # 뒤쪽 칸이 벽이라면 
            stop = True
        else: # 벽이 아니라면 후진
            r = nx
            c = ny

print(answer)
