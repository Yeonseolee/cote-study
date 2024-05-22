N=int(input())

paper=[list(map(int,input().split())) for _ in range(N)]
units=[]
def spliter(n,m,N):
    point = paper[n][m]
    for x in range(n,n+N):
        for y in range(m,m+N):
            if paper[x][y]!=point:
                spliter(n,m,N//2)
                spliter(n+N//2,m,N//2)
                spliter(n,m+N//2,N//2)
                spliter(n+N//2,m+N//2,N//2)
                return
    if point==1:
        units.append(1)
    else:
        units.append(0)
        
spliter(0,0,N)

print(units.count(0))
print(units.count(1))
