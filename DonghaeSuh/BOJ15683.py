from copy import deepcopy

N,M = map(int, input().split())
place = [list(map(int,input().split())) for _ in range(N)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

directions={1:[[0],[1],[2],[3]],
           2:[[0,2],[1,3]],
           3:[[0,1],[1,2],[2,3],[3,0]],
           4:[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
           5:[[0,1,2,3]]}

cctvs=[]
answer=0
for x in range(N):
    for y in range(M):
        if place[x][y] in [1,2,3,4,5]:
            cctvs.append((place[x][y],x,y))
        elif place[x][y]==0:
            answer+=1

def check(x,y):
    return x<0 or x>=N or y<0 or y>=M
            
def move(x,y,copy_place,direction):
    for d in direction:
        nx,ny = x,y
        
        while True:
            nx+=dx[d]
            ny+=dy[d]
            
            if check(nx,ny):
                break
            if copy_place[nx][ny]==6:
                break
            if copy_place[nx][ny]!=0:
                continue
            copy_place[nx][ny]='#'

def count(copy_place):
    global answer
    cnt=0
    for i in copy_place:
        cnt+=i.count(0)
    answer=min(cnt,answer)
    
def backtracking(level,p):
    copy_place=deepcopy(p)
    
    if level==len(cctvs):
        count(copy_place)
        return
    
    point,x,y=cctvs[level]
    
    for d in directions[point]:
        move(x,y,copy_place,d)
        backtracking(level+1,copy_place)
        copy_place=deepcopy(p)
        
backtracking(0,place)
print(answer)
