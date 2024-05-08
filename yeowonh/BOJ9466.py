# 블로그 글 참고
import sys
sys.setrecursionlimit(10**5)

def dfs(node):
    global cnt

    visited[node] = True
    group.append(node)

    # 방문 지점으로 돌아왔다면
    if visited[graph[node]] == True:
        # 사이클이 완성되었을 경우
        if graph[node] in group:
            # 전체 그룹에서 슬라이싱해주기
            cnt -= len(group[group.index(graph[node]):])
        return
    else:
        dfs(graph[node])



T = int(input())

for _ in range(T):
    n = int(input())
    graph = [0] * (n+1)

    numbers = list(map(int, input().split()))
    
    # 인덱스 = 선택하는 학생, 값 = 선택되는 학생
    for idx, num in enumerate(numbers):
        graph[idx + 1] = num

    cnt = n
    visited = [False] * (n+1)
    result = []

    # dfs 수행하기 - 시작 노드 순차적으로 넣어주기
    for start_node in range(1, n+1):
        if visited[start_node] == False:
            group = []
            dfs(start_node)

    print(cnt)
