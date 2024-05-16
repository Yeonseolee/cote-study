import heapq

def solution(jobs):
    answer = 0
    now = 0 #현재시간
    i = 0   #처리개수
    start = -1 #마지막 완료시간
    heap = []
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap,[job[1],job[0]])
        
        if heap:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += now - current[1] #요청으로부터 처리시간
            i += 1
        else:
            now += 1
            
    return answer // len(jobs)



'''

import heapq

# choose_start 은 len(jobs) > 0 일 때 작동하도록 한다.
def choose_start(jobs):
    
    job = heapq.heappop(jobs)
    start = job[0]
    length = job[1]
    
    
    if len(jobs) == 0:
        return start, length, jobs
    
    job_tmp = job
    
    while len(jobs) > 0:
        job = heapq.heappop(jobs)
        
        if start < job[0]:
            heapq.heappush(jobs, job)
            break
        elif start == job[0]:
            if length <= job[1]:
                heapq.heappush(jobs,job)
                break
            else:
                length = job[1]
                heapq.heappush(jobs,job_tmp)
        else:
            start = job[0]
            length = job[1]
            heapq.heappush(jobs,job_tmp)
            break
        
        job_tmp = job
    
    return start, length, jobs


def match_start(start, length, jobs):
    end = start + length
    wait = []
    while jobs:
        job = heapq.heappop(jobs)
        if end >= job[0]:
            wait.append(job)
        else:
            heapq.heappush(jobs,job)
            break
    for w in wait:
        heapq.heappush(jobs,[end,w[1]])
    
    return jobs

def solution(jobs):
    time = 0
    k = len(jobs)
    heapq.heapify(jobs)
    start = 0
    length = 0
    
    while jobs:
        
        # 시작을 선택
        start, length, jobs = choose_start(jobs)
        
        # 시작의 끝에 맞추어 재정렬 
        if len(jobs) > 0:
            jobs = match_start(start, length, jobs)
        else:
            break
    time = start + length
    
    print(time)
    print(k)
    
    return time//k
    
        
jobs = [[0, 3], [1, 9], [2, 6]]

print(solution(jobs))

'''