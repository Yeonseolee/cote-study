"""
이게 뭔 말임..?

A_0 = 1
-> 현재 인덱스를 P와 Q로 나눈 것의 "내림값" 인덱스의 합

A_7 = A_3 + A_2
A_3 = A_1 + A_1
A_1 = A_0 + A_0

-> 전형적인 DP 문제
-> 탑다운
"""
from collections import defaultdict

# 수열 n번째 반환
def dp(n):
    # 저장되어 있는 값이면
    if data[n] != 0:
        return data[n]

    data[n] = dp(n // p) + dp(n // q)
    return data[n]


n, p, q = map(int, input().split())
data = defaultdict(int)
data[0] = 1 # 초기값 작성

print(dp(n))
