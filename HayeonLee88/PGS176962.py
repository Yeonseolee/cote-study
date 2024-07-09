'''
수행 중이거나 멈춘 과제를 탐는 stack
plans = 큐
큐 시작 시간 순으로 정렬하기
스택과 큐가 모두 비면 멈추기
'''
from collections import deque

def solution(plans):
    answer = []
    stack = [] # 수행 중이거나 멈춘 과제를 담는 스택

    # 시작 시간을 분으로 만들기
    for i, (name, start, playtime) in enumerate(plans):
        new = int(start[:2]) * 60 + int(start[-2:])
        plans[i][1] = new

    plans.sort(key = lambda x: x[1]) # 시작 시간 기준으로 정렬
    plans = deque(plans)
    
    now = 0 # 현재 시간
    cnt = 0 # 과제를 하는 시간
    while plans or stack: # plans와 stack이 모두 비면 break
        if stack: 
            if stack[-1][1] == cnt: # 수행 중인 과제가 끝났다면
                name, _ = stack.pop()
                answer.append(name)
                cnt = 0 
                
        if plans:        
            if plans[0][1] == now: # 시작 시간과 현재 시간이 같다면
                if stack: # 수행 중인 과제가 있을 때
                    if stack[-1][1] - cnt > 0: # 남은 과제
                        stack[-1][1] -= cnt 
                    else: # 끝난 과제
                        name, _ = stack.pop()
                        answer.append(name)
                        
                name, start, playtime = plans.popleft()
                stack.append([name, int(playtime)])
                cnt = 0 
                
        now += 1
        cnt += 1
        
    return answer