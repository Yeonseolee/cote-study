# BFS 방식으로 풀어서 시간초과가 난 코드
# 시작 노드로부터 간선 연결 가능
from collections import deque

# 그래프 형성될 경우 그래프에 속한 노드 반환
# 아닐 경우 None 반환
def bfs(graph, start):
    queue = deque()
    visited = [start]
    queue.append(start)

    while queue:
        now = queue.popleft()
        
        # 단 한명만 선택 가능
        if graph[now] not in visited:
            queue.append(graph[now])
            visited.append(graph[now])

        # 시작 지점으로 돌아왔다는 뜻
        if graph[now] == start:
            return visited
    
    return None


T = int(input())

for _ in range(T):
    n = int(input())
    graph = dict()

    numbers = list(map(int, input().split()))
    
    # number들을 딕셔너리에 추가해주기
    for idx, num in enumerate(numbers):
        graph[idx + 1] = num

    group_node = []

    # bfs 수행하기 - 시작 노드 순차적으로 넣어주기
    for start_node in range(1, n+1):
        if start_node not in group_node:
            group = bfs(graph, start_node)
            if group != None:
                group_node += group

    # print('## total group node : ', group_node)
    print(n-len(group_node))