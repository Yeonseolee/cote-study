import copy

def solution(tickets):
    n = len(tickets)
    visited = [False] * (n + 1)
    route = [0] * (n + 1)
    route[0] = "ICN" 

    answer = []
    def DFS(cnt):
        if cnt == n + 1:
            tmp = copy.deepcopy(route)
            answer.append(tmp)
            return
        for i in range(n):
            if route[cnt - 1] == tickets[i][0]:
                if not visited[i]:
                    visited[i] = True
                    route[cnt] = tickets[i][1]
                    DFS(cnt + 1)
                    route[cnt] = 0
                    visited[i] = False

    DFS(1)
    answer.sort()
    return answer[0]