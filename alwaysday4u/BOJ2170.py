import sys
input = sys.stdin.readline

lines = []
for _ in range(int(input())):
    lines.append(tuple(map(int, input().split())))
lines.sort()

prev_x, prev_y = lines[0]
total_len = 0

for i in range(1, len(lines)):
    x, y = lines[i]
    if x < prev_y:
        prev_y = max(y, prev_y)
    else:
        total_len += (prev_y - prev_x)
        prev_x, prev_y = x, y

total_len += (prev_y - prev_x)
print(total_len)
    
