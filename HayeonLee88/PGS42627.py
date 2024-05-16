import heapq
def solution(jobs):
    answer = 0 # 모든 작업이 걸린 시간을 더하는 변수
    now = 0 # 이전 작업이 끝난 후 현재 시간을 나타내는 변수
    heapq.heapify(jobs) # 요청 시점 -> 소요 시간 기준으로 우선순위 정렬
    total = len(jobs)
    for i in range(total):
        start, time = heapq.heappop(jobs)
        if now < start: # 가장 빠른 요청 시점이 현재 시간보다 클 때(이전 작업이 끝난 후 텀이 있을 때)
            answer += time
            now = start + time
        else: # 가장 빠른 요청 시점이 현재 시간보다 작거나 같을 때(이전 작업이 끝난 후 텀이 없을 때)
            tmp = [[start, time]]
            while jobs: # 이전 작업이 시작하고 끝날 때까지 요청된 작업들을 tmp에 담기 위한 반복문
                start, time = heapq.heappop(jobs)
                if start > now: # 이전 작업 이 끝난 후 요청된 작업은 다시 heap에 담고 break
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