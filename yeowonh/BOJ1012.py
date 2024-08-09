# 상하좌우에서 이동 가능 -> bfs로 탐색할 것

# 인접해있는 배추가 몇 덩어리인지 탐색할 것

# 바이러스와 연관짓기 -> 모든 방향이 0으로 둘러쌓여있을 때??
# [0,0][1,0][1,1]
# [1,0][1,1]
# 시작 지점의 인접노드가 아니면서 1일 경우 cnt 1씩
# 1. [0,0] pop하면서 2로 바꾸기
# 2. queue : [1,0]
# 3. q : [1,1]
# 큐가 비었음 -> cnt + 1하고 1발견할때까지 pop할 것

# 기본적인 bfs 탐색으로 가되, queue에서 pop할때 2로 값을 변경해 중복 체크가 되지 않도록 하며 처음에 시작지점을 다 넣어두는 것이 아니라 돌다가 1 발견할 때 체크



from collections import deque

def bfs(graph, m, n):
    cnt = 0
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    queue = deque()

    # 반복문 다 순회할 때까지
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                # 배추 한 덩이
                cnt += 1
                # 첫 1 좌표 넣기
                queue.append([i,j])
                graph[i][j] = 2
                
                # 시작되는 큐 넣기
                while queue:
                    # pop하기
                    x, y = queue.popleft()

                    # 상하좌우 탐색하기
                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy
                        # 우선 유효한 좌표인지?
                        if 0 <= nx < n and 0 <= ny < m:
                            # 방문한 적이 없고 옆에 배추가 있는지?
                            if graph[nx][ny] == 1:
                                queue.append([nx, ny])
                                graph[nx][ny] = 2
            
    return cnt



def solution(t):
    result = []

    # 케이스 t번만큼 입력받음
    for _ in range(t):
        m, n, k = map(int, input().split())
        # 배열 생성
        graph = [[0 for _ in range(m)] for _ in range(n)]
        
        # 배추 맵에 표시하기
        for _ in range(k):
            x, y = map(int, input().split())
            graph[y][x] = 1

        # bfs 수행 후 결과 출력
        result.append(bfs(graph, m, n))
    
    for a in result:
        print(a)

import sys
input = sys.stdin.readline

t = int(input())
solution(t)