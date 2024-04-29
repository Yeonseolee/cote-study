import sys

input = lambda: sys.stdin.readline().rstrip()

K, L = map(int, input().split())
wait_list = {}

for i in range(L):
    num = input()
    wait_list[num] = i

sorted_wait_list = sorted(wait_list.items(), key = lambda x: x[1])

for k, v in sorted_wait_list[:K]:
    print(k)
