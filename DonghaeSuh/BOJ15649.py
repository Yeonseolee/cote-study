# https://www.acmicpc.net/problem/15649
N,M = map(int,input().split())

array=[]
def backtracking():
    if len(array)==M:
        print(' '.join(map(str,array)))
    
    for i in range(1,N+1):
        if i not in array:
            array.append(i)
            backtracking()
            array.pop()
        
backtracking()
