"""
요청부터 종료까지 걸린 시간의 평균을 가장 줄여보자
가장 줄여보려면 어떻게 해야할까?

1. 작업 시간이 동일하다면 먼저 들어온 것을 먼저 처리하기
2. 작업 시간이 길다면 작업 시간이 상대적으로 짧은 것 부터 먼저 처리하기

최소 힙으로 풀기
-> 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터
FIFO (큐)

1. 큐에 작업 하나씩 쌓기
2. 초가 흐를 때마다 해당하는 거 하나씩 꺼내고 누적
3. 대기 시간 = 작업 시작 시간 + 작업 시간 - 요청시간
-> 대기 시간의 평균이 가장 짧아져야 함

[0,3] [1,9] [2,6]

[0, 3, 3] [1, 9, 8] [2, 6, 4]

cur=3

jobs = [[5, 10], [6, 8], [14, 2], [11, 5], [100, 7]]
return = 11

"""
from collections import deque

def solution(jobs):
    answer = []
    # 요청 시점, 소요 시간
    visited = []
    
    # 작업 요청 시간에 따라서 정렬하고 큐에 삽입하기
    jobs.sort(key=lambda x: x[0])
    queue = deque([jobs[0]])
    
    cur = 0 # 현재 시간
    while queue:
        # print('## queue :', queue)
        # 하나씩 꺼내기
        now = queue.popleft()
        # print('## now:', now)
        visited.append(now) # 방문처리
        
        # 총 대기 시간 append하기
        answer.append(cur + now[1] - now[0])
        
        # 시간의 흐름
        cur += now[1]
        
        # cur보다 먼저 요청된 것들만 queue에 삽입하기
        tmp = [x for x in jobs if x[0] <= cur]
        tmp.sort(key=lambda x: x[1])

        for job in tmp:
            if job not in visited:
                queue.append(job)
                visited.append(job)
    
    # 마무리 : 방문 안한 것들
    left = [x for x in jobs if x not in visited]
    left.sort(key= lambda x: x[1])

    for job in left:
        # print('## now:', job)
        # 요청 시간으로 현재 시간 조정
        cur = job[0] 
        answer.append(cur + job[1] - job[0])

    return sum(answer) // len(answer)
