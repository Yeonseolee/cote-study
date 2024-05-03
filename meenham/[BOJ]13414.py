import sys

K, L = map(int, input().split())

id2index = {}

for i in range(L):
    id = sys.stdin.readline().rstrip()
    #id = input()
    id2index[id] = i
        
dict_list = id2index.items()

id_list = list(sorted(dict_list, key = lambda x : x[1] ))

l = min(K, len(dict_list))

for i in id_list[:l]:
    print(i[0])