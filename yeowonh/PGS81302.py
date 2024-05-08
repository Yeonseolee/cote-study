from collections import deque

# 모든 강의실 서칭하면서 하나라도 예외 있으면 return 0
# 모든 시작 지점 통과해야 return 1

def bfs_search(graph):
    # 원본 강의실 copy 및 리스트로의 변환
    graph_copy = []
    for row in graph:
        graph_copy.append([x for x in row])
    
    distance = [[0] * len(graph[0]) for _ in range(len(graph))]
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    start = []
    n, m = len(graph), len(graph[0])
    for i in range(n):
        for j in range(m):
            if graph_copy[i][j] == "P":
                start.append((i, j))

    for s in start:
        queue = deque([s])
        graph_copy[s[0]][s[1]] = 'X'

        while queue:
            y, x = queue.popleft()
            
            # 인접 노드 탐색
            for dx, dy in direction:
                nx = x + dx; ny = y + dy
                
                # 벽 체크 & 방문 체크
                if 0 <= nx < m and 0 <= ny < n and graph_copy[ny][nx] != 'X':
                    # 다른 참가자일 경우 & 맨해튼 거리 2 이하일 경우
                    if graph_copy[ny][nx] == 'P' and distance[y][x] + 1 <= 2:
                        return 0
                    
                    # 방문한 적 없을 경우 큐에 넣고 거리 더해주기
                    if graph_copy[ny][nx] == "O":
                        queue.append([ny, nx])
                        # 미리 방문처리
                        graph_copy[ny][nx] = "X"

                        # 거리 계산
                        distance[ny][nx] = distance[y][x] + 1
            
    # 모든 케이스 통과
    return 1



def solution(places):
    answer = []
    
    # i개의 강의실
    for place in places:
        answer.append(bfs_search(place))
                
    return answer