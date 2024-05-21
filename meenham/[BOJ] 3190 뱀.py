from collections import deque

N = int(input())

K = int(input())

apple_location = []
for _ in range(K):
    apple_location.append(list(map(int, input().split())))

L = int(input())
rotate_list = []
for _ in range(L):
    rotate_list.append(list(input().split()))

direction = {0 : (0,1), 1 : (1,0), 2 : (0,-1), 3 : (-1,0)}

body = deque([[1,1]])

time = 0

# 방향 동쪽부터 시작 
dir = 0 

# rotate 위치 체크
l = 0

def rotate_direction(dir,angle):
    if angle == 'L':
        if dir == 0:
            dir = 3
        else:
            dir -= 1
    if angle == 'D':
        if dir == 3:
            dir = 0
        else:
            dir += 1
    
    return dir        
            
        

while True:
    time += 1
    
    head = body[-1]
    row = head[0]
    col = head[1]
    
    row += direction[dir][0]
    col += direction[dir][1]
    
    # 사과를 먹으면 꼬리의 위치를 남기고 머리 이동, 없으면 꼬리 위치를 제거
    if [row,col] in body:
        break
    
    #벽과 부딪히면 종료
    if row < 1 or row > N or col <1 or col > N : 
        break
    
    if [row,col] in apple_location:
        body.append([row,col])
    else:
        body.append([row,col])
        body.popleft()
    # 자신의 몸과 부딪히면 종료
    
    
    # rotate 에 포함되면 방향 회전
    if l < L:
        if time == int(rotate_list[l][0]):
            dir = rotate_direction(dir,rotate_list[l][1])
            l += 1

print(time)