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

가만히 있어도 되는 경우
-> 맵 전체를 이동시키는 게 아니라 벽 위치만 이동시키자
"""

from collections import deque

def BFS():
    global graph, start, target

    # 위쪽부터 시계방향 회전 (y, x) !! 제자리도 포함해야 함 !!
    direction = [(-1, 0), (-1, 1), (0, 1), 
                 (1, 1), (1, 0), (1, -1), 
                 (0, -1), (-1, -1), (0, 0)]

    # 시작 위치, 목표 위치
    queue = deque()
    queue.append((start[0], start[1]))

    visited = [start] # 시작 위치 방문 처리

    while queue:
        y, x = queue.popleft()
        # 벽일 경우 continue해서 돌아가기
        if graph[y][x] == '#':
            continue

        # 인접 노드 탐색
        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if ny < 0 or ny >= len(graph) or nx < 0 or nx >= len(graph[0]) or graph[ny][nx] == '#':
                continue
            
            # 타깃 처리
            # 벽이 한 칸 내려오는 것 = 욱제가 한 칸 위로 올라가는 것
            # 욱제가 맨 위칸으로 올라가기만 하면, 가장 오른쪽으로 갈 수 있음
            # -> 1초 뒤에는 욱제와 같은 칸에 있는 벽들이 전부 아래로 내려가고,, 욱제는 그 칸에 그대로 있으므로
            if ny == 0:
                return 1
            
            # 욱제 한 칸 위로 이동 = 벽이 한칸 내려감
            if (ny-1, nx) not in visited:
                visited.append((ny-1, nx))
                queue.append((ny-1, nx))
    
    return 0

graph = []
start, target = (7, 0), (0, 7)

for _ in range(8):
    string = input()
    graph.append([x for x in string])


print(BFS())