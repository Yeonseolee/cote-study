import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
location = [ tuple(map(int, input().split())) for _ in range(N)]
location.sort()
line = [[location[0][0], location[0][1]]]
print(location)

for x, y in location:
    for i in range(len(line)):
        if line[i][0] <= x and x <= line[i][1]:
            if y >= line[i][1]:
                line[i][1] = y
            break
    
    if line[-1][1] < x:
        line.append([x, y])
    print(line)

ans = 0
for x, y in line:
    ans += abs(y-x)

print(ans)
            