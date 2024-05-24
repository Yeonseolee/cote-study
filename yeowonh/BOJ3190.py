"""
N*N 정사각 보드 위 / 뱀의 길이는 1
사과 있으면 -> 머리 늘리기, 꼬리 그대로
사과 없으면 -> 꼬리 없애기

종료 조건 : 벽이나 자기 자신의 몸 -> 전까지 몇 초 걸리나 체크
"""

from collections import deque

n = int(input())
k = int(input())

board = [[0] * n for _ in range(n)]

# 오른쪽부터 시계방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 사과 입력
for i in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 2

# 뱀 입력
l = int(input())
dirDict = dict()
queue = deque()
queue.append((0, 0))

# x초 : 방향
for i in range(l):
    x, c = input().split()
    dirDict[int(x)] = c

# 초기값
x, y, time, cur_dir  = 0, 0, 0, 0
board[x][y] = 1

def turn(alpha):
    global cur_dir
    if alpha == 'L':
        cur_dir = (cur_dir - 1) % 4
    else:
        cur_dir = (cur_dir + 1) % 4


while True:
    time += 1
    x += dx[cur_dir]
    y += dy[cur_dir]

    # 벽에 닿을 경우
    if x < 0 or x >= n or y < 0 or y >= n:
        break
    
    # 사과 닿을 경우
    if board[x][y] == 2:
        board[x][y] = 1
        queue.append((x, y))
        if time in dirDict: # 방향 전환 필요한 경우
            turn(dirDict[time])

    # 사과 없을 경우
    elif board[x][y] == 0:
        board[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        board[tx][ty] = 0 # 꼬리 없애기
        if time in dirDict: # 방향 전환 필요한 경우
            turn(dirDict[time])

    # 자신의 몸에 닿을 경우
    else:
        break

print(time)