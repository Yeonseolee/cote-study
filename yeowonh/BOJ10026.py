"""
N*N 크기의 그리드 각 칸에 RGB 중 하나를 색칠한 그림
-> 그림은 몇 개의 구역으로 나뉘는 데 구역은 같은 색으로 이뤄져있음
-> 같은 색상이 인접한 경우 두 글자는 같은 구역 = 같은 영역

이걸 왜 DFS로 풀어야 하지?? BFS 그래프 섬 개수 문제랑 비슷하지 않나

1. 전체 좌표 순회해보기
2. BFS로 인접 노드 순회
3. 색깔 같을 때마다 방문, 좌표 global visited 에 저장
4. queue 탈출하면 +1

DFS로 풀면 더 쉽긴 하겠다

"""
from collections import deque

n = int(input())
graph = [[x for x in input()] for _ in range(n)]

normal_visited = []; color_visited = []
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
result, result_c = 0, 0

def bfs(sy, sx, flag):
    global graph, n, normal_visited, color_visited
    queue = deque()
    queue.append((sy, sx))

    if flag == 'normal':
        visited = normal_visited
    else:
        visited = color_visited

    visited.append((sy, sx))

    while queue:
        y, x = queue.popleft()

        for d in direction:
            ny, nx = y + d[0], x + d[1]
            if 0 <= ny < n and 0 <= nx < n and (ny, nx) not in visited:
                if graph[y][x] == graph[ny][nx]:
                    visited.append((ny, nx))
                    queue.append((ny, nx))
                
                elif flag == 'color' and (graph[y][x] + graph[ny][nx] == 'RG' or graph[y][x] + graph[ny][nx] == 'GR'):
                    visited.append((ny, nx))
                    queue.append((ny, nx))
    
    return visited


for i in range(n):
    for j in range(n):
        if (i, j) not in normal_visited:
            normal_visited = bfs(i, j, 'normal')
            result += 1
        if (i, j) not in color_visited:
            color_visited = bfs(i, j, 'color')
            result_c += 1


print(result, result_c)