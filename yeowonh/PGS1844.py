# 칸의 최솟값
# BFS로 풀고 카운트
# 상하좌우 이동 가능

"""
0,0 시작 -> n, m까지
"0" 이 벽임 / "1"은 진행 가능한 통로
"""

from collections import deque

def bfs(maps, n, m):
    queue = deque()
    queue.append([0, 0, 0])
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    
    # 방문한 곳은 0으로 바꾸기
    maps[0][0] = 0
    
    while queue:
        y, x, result = queue.popleft()
        # n-1, m-1일 때 return
        if y == n-1 and x == m-1:
            return result + 1
        
        
        # 상하좌우 탐색
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            # 맵 벗어나지 않는지
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 0:
                maps[ny][nx] = 0
                queue.append([ny, nx, result + 1])
                
    return -1

def solution(maps):
    return bfs(maps, len(maps), len(maps[0]))