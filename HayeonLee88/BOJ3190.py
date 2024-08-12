'''
문제 읽기 ~ 제출 : 7:34 ~ 8:25

벽 또는 몸과 부딪히면 게임 종료

1. 몸을 늘려 머리를 다음칸에 위치
2. 벽이나 자기자신과 부딪히면 끝
3.1 이동한 칸에 사과가 있다면, 사과가 없어지고 꼬리는 움직이지 않는다.
3.2 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.

보드 크기: NxN 
K: 사과 개수
L: 방향 전환 횟수
X C: 방향 전환 정보 
    X초, C==L 왼쪽 / C==D 오른쪽 
* 행과 열은 1부터 시작
* 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

사과의 위치와 뱀의 이동경로가 주어질 때 게임이 끝나는 시간을 계산

solution
- 뱀의 몸을 depue을 사용하여 queue로 구현한다.
- 뱅의 방향 전화 정보를 depue을 사용하여 queue로 구현한다.
- 보드의 가장자리에 바깥을 두른다.
- 바깥 -1, 빈 공간 0, 사과 1
    - 뱀의 머리를 방향에 맞게 움직인다.
    - 머리의 위치가 deque에 있거나 바깥으로 벗어나면 종료
    - 이동한 곳에 사과가 있다면 그대로
    - 이동한 곳에 사과가 없다면 popleft()

코드 짜기 ~ 종료: 7:43 ~ 8:25
'''
import sys
from collections import deque

input = lambda:sys.stdin.readline().rstrip()

n = int(input())
# 보드
graph = [[-1] * (n + 2)]

for i in range(1, n + 1):
    graph.append([-1])
    graph[i].extend([0] * n)
    graph[i].append(-1)

graph.append([-1] * (n + 2))

# 사과 위치 
k = int(input())
for i in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1

l = int(input())
# 방향 전환 정보
dirs = deque(list(input().split()) for _ in range(l))

# 이동 방향 (오른쪽부터 시계방향)
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

dir = {'L': -1, 'D': 1}

def dos(x, y):
    q = deque()
    q.append((1, 1))
    cnt = 0 # 시간
    idx = 0 # 이동방향 인덱스
    x, y = q[0]
    while True:
        cnt += 1
        nx = x + dx[idx]
        ny = y + dy[idx]
        # 이동한 곳에 몸이 있거나 바깥을 벗어나면 break
        if (nx, ny) in q or graph[nx][ny] == -1:
            break
        # 사과가 있을 때
        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
        # 사과가 없을 때
        else:
            q.popleft()
        q.append((nx, ny))
        x, y = nx, ny
        # 방향 정보가 있을 때 현재 시간과 일치한다면
        if dirs:
            if cnt == int(dirs[0][0]):
                _, c = dirs.popleft()
                idx += dir[c]
                idx %= 4 # 처음에 빼먹어서 idex error가 낫었다..
    return cnt

print(dos(1, 1))