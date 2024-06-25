import sys

input = sys.stdin.readline

N,M = map(int,input().split())

r,c,dir = map(int,input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

direction = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}

clean = 0

x = r
y = c

def clean_around():
    for i in range(4):
        if graph[x+direction[i][0]][y+direction[i][1]] == 0:
            return False
    return True
    
while True:
    
    if graph[x][y] == 0:
        graph[x][y] = 2
        clean += 1
    
    result = clean_around()    
    
    if result == False:
        while True:
            dir -= 1
            if dir <0 : dir += 4
        
            nx = x + direction[dir][0]
            ny = y + direction[dir][1]
        
            if graph[nx][ny] == 0:
                x = nx
                y = ny
                clean += 1
                graph[x][y] = 2
                break
        
        
    elif result == True:
        nx = x - direction[dir][0]
        ny = y - direction[dir][1]
        if graph[nx][ny] != 1:
            x = nx
            y = ny
        else:
            break

print(clean)
        
        
        
        
    
    
                 
    