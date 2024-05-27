from math import ceil
n, a, b, c, d = map(int, input().split())

answer = int(1e18)

if b / a < d / c:
    n1, m1, n2, m2 = a, b, c, d
else:
    n1, m1, n2, m2 = c, d, a, b

check = False
for i in range(n1):
    tmp = ceil((n - i * n2) / n1)
    if tmp < 0:
        tmp = 0
        check = True
    answer = min(answer, i * m2 + tmp * m1)
    if check:
        break

print(answer)