# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    routes.sort(key=lambda x: x[1])
    _, end = routes[0]
    cnt=1
    
    for s,e in routes:
        if s>end:
            cnt+=1
            end=e

    return cnt
