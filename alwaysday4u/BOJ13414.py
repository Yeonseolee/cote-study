import sys

k, l = map(int, input().split())
idx_dict = dict()

for i in range(l):
    idx_dict[sys.stdin.readline().rstrip()] = i

sorted_ids = sorted(idx_dict.keys(), key=lambda x: idx_dict[x])[:k]

for i in sorted_ids:
    print(i)
