'''
7:57~8:07

solution
    - deque으로 큐를 구현하여 bfs로 풀기
    - vistied: 방문한 곳의 거리를 담는 배열, -1로 초기화 
    - 현재 위치에서 상하좌우를 보고 맵을 벗어나지 않으면서, 처음 방문하고, 벽이 아닌 곳일 때 다음 위치를 담는다.
    - visited[n - 1][m - 1] 리턴
'''
from collections import deque

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    visited = [[-1] * m for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = 1
        while q:
            x, y = q.popleft()
            dist = visited[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 경로를 벗어난 경우
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                # 이미 방문한 경우
                if visited[nx][ny] != -1:
                    continue
                # 벽인 경우
                if not maps[nx][ny]:
                    continue
                q.append((nx, ny))
                visited[nx][ny] = dist + 1
        
        return visited[n- 1][m - 1]
    
    return bfs(0, 0)
