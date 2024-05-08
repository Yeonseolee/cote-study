"""
사각지대를 최소화하기
브루트포스니까 모든 경우의 수 전부 비교

1. 감시 당하는 부분 #으로 표시
2. CCTV 좌표 저장해두고, 하나씩 회전해보기
3. 사각지대 최소값 저장

0 -> 3 (시계방향 회전)

"""
import sys
import copy

# CCTV 방향
rotation = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0,1,2,3]]
]

# dx, dy 시계방향 (북 ~ 서)
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def fill(graph, y, x, rotate):
    n = len(graph); m = len(graph[0])
    for i in rotate:
        ny = y; nx = x
        while True:
            ny += direction[i][1]
            nx += direction[i][0]
            # 벽이면 중단
            if nx < 0 or ny < 0 or ny >= n or nx >= m or graph[ny][nx] == '6':
                break
            elif graph[ny][nx] == '0':
                graph[ny][nx] = '#'

def dfs(depth, graph, cctv):
    global min_area

    # 탐색 완료
    if depth == len(cctv):
        min_area = min(check_area(graph), min_area)
        return

    graph_copy = copy.deepcopy(graph)
    y, x, cctv_num = cctv[depth]
    for r in rotation[int(cctv_num)]:
        fill(graph_copy, y, x, r)
        dfs(depth+1, graph_copy, cctv)
        # 보드 초기화
        graph_copy = copy.deepcopy(graph)


# 전체 면적 체크
def check_area(graph):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '0':
                cnt += 1
    return cnt


def solution(n, m):
    graph = []
    cctv = [] # (y, x, num)

    for _ in range(n):
        graph.append(sys.stdin.readline().rstrip().split())
    
    # 초기 그래프 표시 & CCTV 위치 저장
    for i in range(n):
        for j in range(m):
            if graph[i][j] != '0' and graph[i][j] != '6':
                cctv.append([i, j, graph[i][j]])

    # dfs 진행
    dfs(0, graph, cctv)
    return

n, m = map(int, input().split())
min_area = n*m
solution(n, m)
print(min_area)
