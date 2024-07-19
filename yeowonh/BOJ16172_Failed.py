"""
S = input()
K = input()

s = ''.join([x for x in S if x.isalpha()])

print(1 if s.find(K) != -1 else 0)
"""

# 여전히 시간초과 발생..
def solution(S, K):
    s = ''.join([x for x in S if x.isalpha()])

    # 하나씩 밀면서 filtered_s에서 K 찾기
    for i in range(len(s) - len(K) + 1):
        if s[i:i + len(K)] == K:
            return 1
        
    return 0

S = input()
K = input()

print(solution(S, K))