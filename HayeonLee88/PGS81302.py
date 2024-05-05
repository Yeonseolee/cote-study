from collections import deque

def solution(places):
    answer = [1, 1, 1, 1, 1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(p, x, y):
        cnt = 0
        q = deque()
        q.append((x, y, cnt))
        visited[x][y] = True
        while q:
            x, y, cnt = q.popleft()
            cnt += 1
            if cnt == 3:
                break
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx > 4 or ny < 0 or ny > 4: # 구간을 벗어낫을 때
                    continue
                if places[p][nx][ny] == "X" or visited[nx][ny]: # 현재 위치가 칸막이거나 이미 방문한 경우
                    continue
                if places[p][nx][ny] == "P": # 최단 거리가 2이하이면서 현재 위치에 사람이 있을 때
                    return 0
                q.append((nx, ny, cnt))
                visited[nx][ny] = True
        return 1   
    
    for i in range(5):
        visited = [[False] * 5 for _ in range(5)]
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == "P":
                    answer[i] = bfs(i, j, k)
                    if answer[i] == 0:
                        break
            if answer[i] == 0:
                break
    return answer