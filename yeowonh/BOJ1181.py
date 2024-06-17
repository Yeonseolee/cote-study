from functools import cmp_to_key

# print("bbb" < "cbb")
"""
길이가 짧은 것부터 -> 이후 사전순
"""

def compare(w1, w2):
    if len(w1) < len(w2):
        return -1
    elif len(w1) > len(w2):
        return 1
    else:
        if w1 < w2:
            return -1
        else:
            return 1

n = int(input())
word_list = [input() for _ in range(n)]

# 중복 제거
word_list = sorted(list(set(word_list)), key=cmp_to_key(compare))

for word in word_list:
    print(word)