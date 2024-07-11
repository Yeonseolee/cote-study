from collections import defaultdict

N = int(input())


L = defaultdict(list)
j = 0

L[j] = [str(i) for i in range(10)]

while True:
    cnt = len(L[j])
    if N < cnt:
        print(L[j][N])
        break
    N = N - len(L[j])
    for i in L[j]:
        if int(i[0]) != 9:
            for k in range(int(i[0])+1,10):
                L[j+1].append(str(k)+i)
    L[j+1].sort()
    j+= 1
    if len(L[j]) == 0:
        print(-1)
        break 
