"""
시작 지점 -> 가장 왼쪽 아랫칸
목표 지점 -> 가장 오른쪽 윗칸

캐릭터는 상하좌우 & 대각선 이동 가능 / 현재 위치 서있기

벽이 움직여?
- 1초마다 모든 벽이 아래 있는 행으로 한 칸씩 내려감 (가장 밑에서 사라짐)

목표 지점으로 이동할 수 있는지 없는지 여부 확인

1. 그래프 입력 받기
2. while문 반복하면서 그래프 내의 벽 이동 (이동 함수 별도로 만들기)
3. bfs 솔루션 실행하면서 목적지까지 도달 가능한지 확인하기
    3-1. 캐릭터가 먼저 이동 -> 벽이 이동
    3-2. 벽이 캐릭터와 닿으면 바로 0 반환
4. 최종적으로 도달 가능하면 1 반환하기
"""

from collections import deque

def print_graph():
    global graph
    print('#' * 10)
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            print(graph[i][j], end=' ')
        print('')


def move_wall():
    global graph
    # 행 하나씩 밑으로 밀기
    graph.insert(0, ['.','.','.','.','.','.','.','.'])
    graph = graph[:-1]
    return

def BFS():
    global graph, start, target

    # 위쪽부터 시계방향 회전 (y, x)
    direction = [(-1, 0), (-1, 1), (0, 1), 
                 (1, 1), (1, 0), (1, -1), 
                 (0, -1), (-1, -1)]

    # 시작 위치, 목표 위치, 시간
    queue = deque()
    queue.append((start[0], start[1], 0))

    visited = [start] # 시작 위치 방문처리
    prev_time = 0

    # 방문한 곳은 '#' 으로 바꿔주기
    while queue:
        y, x, cur_time = queue.popleft()

        # target 도달
        print('## cur :', y, x, 'target : ', target, 'cur_time : ', cur_time, 'prev_time : ', prev_time)
        if (y, x) == target:
            return 1
        
        # 맵 움직이고 위치 확인
        # 시간의 흐름이 있었다면 맵 움직이기
        if prev_time != cur_time:
            move_wall()
            print_graph()
        
        # 움직인 벽에 닿으면 게임 오버
        if graph[y][x] == '#':
            return 0

        # 인접 노드 탐색
        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if 0 <= ny < len(graph) and 0 <= nx < len(graph[0]) and graph[ny][nx] == '.' and (ny, nx) not in visited:
                prev_time = cur_time
                queue.append((ny, nx, cur_time + 1))
                visited.append((ny, nx)) # 방문 처리
    
    return 0


graph = []
start, target = (7, 0), (0, 7)

for _ in range(8):
    string = input()
    graph.append([x for x in string])


print(BFS())