def DFS(dep, graph, result):
    # 갈 수 있는 공항 탐색
    for arr in graph[dep]:
        # 아직 해당 티켓이 남았다면
        if graph[dep][arr]> 0:
            # 찾아서 1 감소
            graph[dep][arr] -= 1
            DFS(arr, graph, result)
    
    result.append(dep) # 목적지 추가

    return result

from collections import defaultdict
"""
단방향 그래프 -> DFS 탐색 수행

중복 등장횟수까지 그래프에 포함하자!
-> 해당 티켓을 딕셔너리 형태의 개수로 카운트

기존 방식 : (dep, arr) = 1
바꾼 방식 : dep : {'arr' : 1}
"""

def solution(tickets):
    graph = defaultdict(dict)

    for dep, arr in tickets:
        if dep not in graph.keys():
            graph[dep][arr] = 1 # 등록
        else:
            if arr not in graph[dep].keys():
                graph[dep][arr] = 1 # 등록
            else:
                graph[dep][arr] += 1 # 추가
    
    # 알파벳 순서 앞서는 경우 먼저
    for key in graph.keys():
        graph[key] = dict(sorted(graph[key].items()))

    answer = DFS('ICN', graph, [])
    answer.reverse() # 스택 형태이므로 다시 뒤집어서 꺼내줌
    
    return answer