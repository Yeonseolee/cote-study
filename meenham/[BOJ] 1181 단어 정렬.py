import sys


from collections import defaultdict

input = sys.stdin.readline

N = int(input())

dict = defaultdict(list)

for _ in range(N):
    s = input().rstrip()
    l = len(s)
    
    dict[l].append(s)

for i in range(1,N+1):
    if len(dict[i]) != 0:
        dict[i].sort()
        k = 0
        for j in dict[i]:
            if j != k:
                print(j)    
            k = j