from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0 # 경과 시간
    total_weight = 0 # 다리 위 트럭들의 무게
    truck_weights = deque(truck_weights)
    passing = deque() # 다리 위에 있는 트럭을 담는 큐

    while True:
        time += 1
        # 다리 위에 트럭이 있다면
        if passing:
            if passing[0][1] + bridge_length == time: # 맨 앞 트럭이 다리를 다 건넜다면
                truck_weight, _ = passing.popleft()
                total_weight -= truck_weight
                
        # 대기 중인 트럭이 있을 때
        if truck_weights:
            if total_weight + truck_weights[0] <= weight: # 다리 위의 무게가 제한을 넘지 않는다면
                truck_weight = truck_weights.popleft()
                passing.append([truck_weight, time])
                total_weight += truck_weight
        # 다리 위에 트럭이 없을 때
        if not passing:
            break
            
    return time