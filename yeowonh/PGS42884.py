def solution(routes):
    answer = 0
    # (진입 시점, 진출 시점)
    # 진출 시점 기준으로 정렬 잡고
    routes.sort(key=lambda x:x[1])
    cam = -30001 # 초기 위치 설정
    
    for route in routes:
        # 감시카메라가 진입시점보다 작을 경우 못 만난 것
        # 감시카메라 한 대 추가하고 감시카메라 위치 진출 시점으로 변경
        if cam < route[0]:
            answer += 1
            cam = route[1]
    
    return answer