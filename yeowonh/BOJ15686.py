"""
크기 N*N
브루트포스
1. 치킨 거리 구하는 함수
2. 치킨 집 위치 좌표 넣기
3. 해당 치킨 집 위치를 제외하고 모두 없앤 가상맵 생성 함수
3. 가상 하나씩 돌면서 모든 경우의 수에 대해 치킨 거리를 계산

"""
from itertools import combinations
import sys

def chicken_dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

# 해당 맵에서의 치킨 거리 합
def calc_sum_dist(stores):
    global houses, N
    sum_dist = 0

    for house in houses:
        min_dist = 10**6

        for store in stores:
            # 집과 가장 가까운 치킨집 거리
            min_dist = min(min_dist, chicken_dist(house[0], house[1], store[0], store[1]))
        sum_dist += min_dist

    return sum_dist


chicken_store = []
houses = []

N, M = map(int, input().split())
graph = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]
# print(graph)

min_dist = 10**6

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 2:
            chicken_store.append([i, j])
        elif graph[i][j] == 1:
            houses.append([i, j])

chicken_combi = list(combinations(chicken_store, M))

# 전체 맵에서의 치킨 거리 최소값
for stores in chicken_combi:
    min_dist = min(min_dist, calc_sum_dist(stores))

print(min_dist)