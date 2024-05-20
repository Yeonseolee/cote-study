from itertools import combinations

def manhatan(arr1,arr2):
    return abs(arr1[0]-arr2[0]) + abs(arr1[1]-arr2[1])

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house_list = [(i,j) for i in range(N) \
              for j in range(N) if city[i][j] == 1]
chicken_list = [(i,j) for i in range(N) \
                for j in range(N) if city[i][j] == 2]

min_distance = float('inf')

for comb in combinations(chicken_list, min(M, len(chicken_list))):
    total_distance = 0
    for house in house_list:
        min_distance_local = float('inf')
        for chicken in comb:
            distance = manhatan(house, chicken)
            min_distance_local = min(distance, min_distance_local)
        total_distance += min_distance_local
    min_distance = min(total_distance, min_distance)
        
print(min_distance)
