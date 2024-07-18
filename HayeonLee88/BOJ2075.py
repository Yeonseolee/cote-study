import sys
import heapq

input = lambda:sys.stdin.readline().rstrip()

n = int(input())

array = []

for _ in range(n):
    for x in list(map(int, input().split())):
        heapq.heappush(array, x)
        if len(array) > n:
            heapq.heappop(array)

print(heapq.heappop(array))