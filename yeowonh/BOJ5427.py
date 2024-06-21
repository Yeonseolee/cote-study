"""
동서남북으로 퍼져나감
벽에는 불 X -> 불이 옮겨진 칸 / 불이 붙으려는 칸으로 이동 X
상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있음
얼마나 빨리 빌딩 탈출 가능?

불을 먼저 붙이기 -> 사람이 그래프 밖으로 나갈 수 있는가
각 경로마다 불이 붙는 시간을 기록하고 상근이가 지나갈 수 있는 시간인지 판단
"""
from collections import deque

def fire():
    global w, h, graph, direction
    queue = deque()
    fire_time = [[-1 for _ in range(w)] for _ in range(h)]

    # 초기 불 위치
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                queue.append((i, j, 1))
                fire_time[i][j] = 1 # 초기 불 위치
    
    while queue:
        y, x, t = queue.popleft()

        for i in range(4):
            ny = y + direction[i][0]
            nx = x + direction[i][1]

            # 그래프 안쪽 & 벽이 아니고 & 방문한적이 없다면
            if 0 <= ny < h and 0 <= nx < w and graph[ny][nx] != '#' and fire_time[ny][nx] == -1:
                fire_time[ny][nx] = t + 1
                queue.append((ny, nx, t+1))

    return fire_time
        
def find_start(w, h, graph):
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                return (i, j, 1)


def bfs():
    global w, h, graph, direction, fire_time
    queue = deque()
    queue.append(find_start(w, h, graph))
    # print('## queue', queue)
    visited = [[0 for _ in range(w)] for _ in range(h)]

    while queue:
        y, x, t = queue.popleft()
        
        # 탈출 조건 -> 몇 초에 탈출했는지
        if y == h - 1 or x == w - 1 or x == 0 or y == 0:
            return t
        
        for i in range(4):
            ny = y + direction[i][0]
            nx = x + direction[i][1]

            # 그래프 안쪽이고, 방문한적이 없으며 그래프가 벽이 아닐ㄹ 때
            if 0 <= ny < h and 0 <= nx < w and visited[ny][nx] == 0 and graph[ny][nx] != '#':
                # 불이 붙기 전 시간이거나 불이 붙은 적이 없을 경우
                if t + 1 < fire_time[ny][nx] or fire_time[ny][nx] == -1:
                    queue.append((ny, nx, t+1))
                    visited[ny][nx] = 1

    return 'IMPOSSIBLE'


result = []
n = int(input())

for _ in range(n):
    w, h = map(int, input().split())
    graph = [[x for x in input()] for _ in range(h)]
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    fire_time = fire()

    result.append(bfs())

print(*result, sep='\n')