from itertools import permutations

n, m = map(int, input().split())
L = [i+1 for i in range(n)]
for perm in permutations(L, m):
    for i in range(m):
        print(perm[i], end = " ")
    print()
