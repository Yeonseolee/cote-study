N, A, B, C, D = map(int, input().split())
x1, x2 = 0,0
min_cost = 10**18

# 완전탐색 -> 시간초과
for x1 in range(10**5):
    for x2 in range(10**5):
        # 개수가 충족되면
        if x1 * A + x2 * C >= N:
            min_cost = min(x1*B + x2*D, min_cost)
            break

print(min_cost)
