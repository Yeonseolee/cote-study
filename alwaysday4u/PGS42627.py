import heapq

def solution(jobs):
    now = 0        # 현재 시간
    complete = 0   # 완료된 작업의 수
    heap = []      # 작업 지속 시간 기준으로 최소값 우선 추출(최소 힙)
    total = 0      # 모든 작업의 대기 시간
    start = -1     # 마지막으로 작업이 시작된 시간 
    
    while complete < len(jobs):
        for job in jobs:
            # 현재 시점에 시작할 수 있는 작업을 힙에 추가
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
                
        if heap:
            work = heapq.heappop(heap) # 소요시간 짧은 작업 시작
            start = now
            now += work[0]             # 작업 후 시간
            total += now - work[1]     # 총 대기시간
            complete += 1
        else:
            now += 1    # 힙에 작업이 없는 경우 현재 시간 + 1
    
    return total // len(jobs)
