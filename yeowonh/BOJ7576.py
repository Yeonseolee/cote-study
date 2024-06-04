# BFS 
# 며칠이 지나면 다 익게 되는지 최소일 수!!
# 상하좌우만 다 익게됨

from collections import deque

def BFS(m, n, box):
    queue = deque()

    for x in range(n):
        for y in range(m):
            if box[x][y] == 1:
                queue.append([x, y])
    
    while queue:
        x, y = queue.popleft()
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            # 벽이 아니고 방문한적 없는 경우
            if 0 <= x < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append([nx, ny])

    return box


def solution(m, n, box):
    answer = 0
    box = BFS(m,n,box)

    # 최소 일 수
    for x in range(n):
        for y in range(m):
            # 안익은거 있을 경우
            if box[x][y] == 0:
                return -1
        # 일수 갱신
        answer = max(answer, max(box[x]))
    return answer - 1


# m은 상자 가로 칸, n은 상자 세로 칸
m, n = map(int, input().split())
box = []

for _ in range(n):
    box_line = list(map(int, input().split()))
    box.append(box_line)

print(solution(m,n,box))
