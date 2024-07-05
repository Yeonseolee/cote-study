"""
N*M 2차원 배열 (0, 0) -> (N-1, M-1)
청소기는 바라보는 방향 -> 북 동 남 서 0 1 2 3
1. 현재 칸이 청소 X 경우 -> 현재 칸 청소
2. 주변 4칸 중 청소 X가 없는 경우
2-1. 방향 유지, 한칸 후진 -> 후진 불가 경우 작동 X

3. 빈칸 있는 경우
3-1. 반시계방향 회전
3-2. 청소되지 않은 경우 한 칸 전진

청소된 칸은 2로 표시하기 -> visited 역할

"""
from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
cnt = 0

# 북동남서
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

queue = deque()
# 큐에 시작 좌표, 현재 방향 추가
queue.append([r, c, d])

while queue:
    y, x, cur_d = queue.popleft()

    # 청소 안된 경우
    if graph[y][x] == 0:
        graph[y][x] = 2; cnt += 1 # 방문 처리

    # 인접 4칸 탐색 -> 현재 방향으로부터 '반'시계방향으로
    cleaned = False
    for i in range(1, 5):
        new_d = (cur_d - i) % 4
        dy, dx = direction[new_d]
        ny, nx = y + dy, x + dx

        # 청소되지 않은 빈 칸인 경우
        if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0:
            queue.append([ny, nx, new_d])
            cleaned = True
            break
    
    # 청소되지 않은 빈 칸이 없는 경우
    if cleaned == False:
        dy, dx = direction[cur_d] # 한 칸 후진
        ny, nx = y - dy, x - dx
        # 한 칸 후진하기 혹은 종료 - 청소한 칸으로도 후진은 가능
        if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] != 1:
            queue.append([ny, nx, cur_d]) # 방향은 유지
        else:
            # 벽에 부딪히면 반복문 탈출
            break

print(cnt)
