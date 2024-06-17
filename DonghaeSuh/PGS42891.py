def solution(food_times, k):
    idx=0
    num=len(food_times)
    
    if sum(food_times) <= k:
        return -1
    
    while k:
        if food_times[idx]:
            food_times[idx]-=1
            k-=1
            if idx<num-1:
                idx+=1
            else:
                idx=0
        else:
            if idx<num-1:
                idx+=1
            else:
                idx=0
    
    while food_times[idx]==0:
        if idx<num-1:
            idx+=1
        else:
            idx=0
                
    return idx+1
