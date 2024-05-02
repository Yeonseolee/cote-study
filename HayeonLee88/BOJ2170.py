import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

lines = [list(map(int, input().split())) for _ in range(N)]
answer = 0

lines.sort()
tmp_x, tmp_y = -1000000000, -1000000000

for x, y in lines:
    if tmp_y <= x: # 앞에 그은 선과 겹치지 않을 때
        answer += (tmp_y - tmp_x)
        tmp_x = x
        tmp_y = y
    else: # 앞에 그은 선과 겹칠 때
        tmp_y = max(tmp_y, y)

answer += (tmp_y - tmp_x)
print(answer)
    