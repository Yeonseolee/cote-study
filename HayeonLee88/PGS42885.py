'''

보트는 한 번에 최대 2명씩
보트 무게 제한 존재
무게 정렬 후 deque으로 큐를 구현
제일 무거운 것과 제일 가벼운 무게를 더하여 무게 제한에 안 걸리면 pop popleft
무게 제한을 넘는 다면 제일 끝만 pop

'''
from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
    while True:
        answer += 1
        if len(people) > 1:
            if people[0] + people[-1] <= limit:
                people.popleft()
            people.pop()
        else:
            break
            
    if not people:
        answer -= 1
        
    return answer