def solution(routes):
    answer = 1
    routes.sort()
    prev_x, prev_y = routes[0]
    for i in range(1, len(routes)):
        x, y = routes[i]
        if x > prev_y:
            prev_x, prev_y = x, y
            answer += 1
        else:
            prev_x, prev_y = x, min(y, prev_y)

    return answer
