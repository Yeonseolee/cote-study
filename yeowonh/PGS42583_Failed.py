"""
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는가
- 다리에는 트럭이 최대 bridge_length대 올라갈 수 있고, 다리는 weight 이하까지의 무게를 견딜 수 있음
"""
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    
    # 대기 트럭이 모두 빠질 때까지
    while len(truck_weights)  > 0 or sum(bridge) > 0:
        truck = bridge.popleft()
        
        # 대기 트럭이 있고 새로운 트럭이 올라갈 수 있으면
        if truck_weights and sum(bridge) + truck_weights[0] <= weight:
            new_truck = truck_weights.popleft()
            bridge.append(new_truck)
        else:
            bridge.append(0)
        
        time += 1
    
    return time