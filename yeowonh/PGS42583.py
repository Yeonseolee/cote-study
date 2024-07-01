"""
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는가
- 다리에는 트럭이 최대 bridge_length대 올라갈 수 있고, 다리는 weight 이하까지의 무게를 견딜 수 있음

"""
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    # 시간 초과 이슈로 bridgeWeight 추가
    time, bridgeWeight = 0, 0
    
    # 대기 트럭이 모두 빠질 때까지
    while len(truck_weights)  > 0 or bridgeWeight > 0:
        bridgeWeight -= bridge.popleft()
        
        # 대기 트럭이 있고 새로운 트럭이 올라갈 수 있으면
        if truck_weights and bridgeWeight + truck_weights[0] <= weight:
            new_truck = truck_weights.popleft()
            bridgeWeight += new_truck
            bridge.append(new_truck)
        else:
            # 다리 길이 채우기
            bridge.append(0)
        
        time += 1
    
    return time