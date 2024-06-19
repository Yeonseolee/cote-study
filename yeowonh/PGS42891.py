import heapq

def solution(food_times, k):
    # 애초에 먹을 음식 안남으면ㄴ
    if k >= sum(food_times):
        return -1
    
    food_list = []
    length = len(food_times) # 남은 음식 개수

    for i in range(length):
        heapq.heappush(food_list, [food_times[i], i+1])
    
    time = 0
    while (food_list[0][0] - time) * length < k:
        k -= (food_list[0][0] - time) * length
        time += food_list[0][0] - time
        length -= 1
        heapq.heappop(food_list)

    result = sorted(food_list, key = lambda x: x[1])
    answer = result[k % length][1]

    return answer