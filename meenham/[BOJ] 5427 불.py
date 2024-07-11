import sys
from collections import deque

input = sys.stdin.readline()

N = int(input())

results = []

for _ in range(N):
    w, h = input().split()
    graph = []
    for _ in range(h):
        graph.append(input().split())
    
    result = function(graph, w, h)
    result.append(result)


def function(graph, w, h):
    
    fires = []
    walls = []
    
    visited =[[False]*w for _ in range(h)]
    
    for i, row in enumerate(graph):
        for j, r in enumerate(row):
            if r == "@":
                start = (i,j)
                visited[i][j] = True
                queue = deque((i,j))
            elif r =="*":
                fires.append((i,j))
            elif r =="#":
                walls.append((i,j))
    
    
    
    
    
    
    
    
    
                
    
    
    
    


for i in results:
    print(result)