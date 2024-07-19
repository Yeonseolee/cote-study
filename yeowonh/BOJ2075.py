"""
N번째 큰 수 ???
5번째"로" 큰 수

힙 이용하기
-> N개의 큰 수 저장
-> N개만 저장하고 더 큰 수 들어오면 작은 수는 pop
"""

import heapq
import sys

N = int(input())
min_heap = []

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for num in row:
        # 힙에 N개보다 적게 있을 경우 계속 넣기
        if len(min_heap) < N:
            heapq.heappush(min_heap, num)
        else:
            # 힙에서 가장 작은 항목을 pop하고 현재 숫자 (더 큰거) 넣기 -> N번째 큰 수들만 오름차순으로 저장됨
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

print(min_heap[0])