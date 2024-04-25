import sys

input = lambda: sys.stdin.readline().rstrip()

n, s = map(int, input().split())
seq = list(map(int, input().split()))

answer = 100001
end = 0
interval_sum = 0
for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += seq[end]
        end += 1
    if interval_sum >= s:
        answer = min(answer, end - start)
    interval_sum -= seq[start]

print(0 if answer == 100001 else answer)