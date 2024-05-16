"""
길이가 M인 수열을 모두 구하는 프로그램
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
-> 순열 사전 순으로 증가하는 순서 출력
"""
from itertools import permutations

n, m = map(int, input().split())
numbers = range(1, n+1)
permut = list(permutations(numbers, m))
permut.sort()

for p in permut:
    for num in p:
        print(num, end=' ')
    print()