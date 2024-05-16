import heapq
def solution(jobs):
    answer = 0
    now = 0
    heapq.heapify(jobs)
    total = len(jobs)
    for i in range(total):
        start, time = heapq.heappop(jobs)
        if now < start: # 가장 빠른 요청 시점이 현재 시간보다 클 때
            answer += time
            now = start + time
        else: # 가장 빠른 요청 시점이 현재 시간보다 작거나 같을 때
            tmp = [[start, time]]
            while jobs:
                start, time = heapq.heappop(jobs)
                if start > now:
                    heapq.heappush(jobs, [start, time])
                    break
                tmp.append([start, time])
            tmp.sort(reverse = True, key = lambda x: x[1]) # 수행 가능한 작업들 중 소요 시간이 가장 작은 작업을 수행하기 위한 정렬
            start, time = tmp.pop()
            answer += (now + time - start)
            now += time
            for start, time in tmp:
                heapq.heappush(jobs, [start, time])
    return answer // total