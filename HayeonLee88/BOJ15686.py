'''
도시의 칸: (r, c) 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸
	0: 빈 칸
    1: 집
    2: 차킨집
치킨 거리: 집과 가장 가까운 치킨집 사이의 거리
도시의 치킨 거리: 모든 집의 치킨 거리의 합
	임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|

도시에 있는 치킨집 중에서 최대 M개를 골라 어떻게 하면 도시의 치킨 거리가 가장 작게 될지 구하시오
N(2 ≤ N ≤ 50), M(1 ≤ M <= 치킨집 ≤ 13) 1<= 집 < 2N

ex) 치킨집 13개, M은 6, 집은 100개
    13C6 = 13 x 11 x 3 x 4 = 1716
    100 * 1716 * 6 = 1,029,600
'''
import sys
from itertools import combinations

INF = 1e9
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = []
houses = [] # 집들의 위치를 담는 리스트
chickens = [] # 치킨집들의 위치를 담는 리스트
for i in range(n):
    graph.append(list(map(int, input().split())))   
    for j in range(n):
        x = graph[i][j]
        if x == 1:
            houses.append([i, j])
        elif x == 2:
            chickens.append([i, j])
picked_combis = list(combinations(chickens, m)) # M개의 치킨집 고르기

answer = INF
for combi in picked_combis: # 각 M개의 치킨집 combination에 대하여 모든 집과의 거리 구하기
    total_dist = 0
    for house in houses:
        dist = 100
        for chicken in combi:
            dist = min(dist, abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]))
        total_dist += dist
    answer = min(answer, total_dist)
    
print(answer)