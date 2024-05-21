import itertools

def min_distance(loc, chicken_loc):
    distance = 10000
    for location in chicken_loc:
        x = abs(loc[0] - location[0])
        y = abs(loc[1] - location[1])
        distance = min(x+y, distance)
    
    return distance

N, M = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

house_loc = []
chicken_loc = []


for row in range(N):
    for col in range(N):
        if graph[row][col] == 1:
            house_loc.append([row,col])
        if graph[row][col] == 2:
            chicken_loc.append([row,col])

comb_chicken_loc = itertools.combinations(chicken_loc,M)

answer_list = []

for chicken_loc in comb_chicken_loc:
    total_distance = 0
    
    for loc in house_loc:
        dis = min_distance(loc,chicken_loc)
        total_distance += dis
    
    answer_list.append(total_distance)

print(min(answer_list))