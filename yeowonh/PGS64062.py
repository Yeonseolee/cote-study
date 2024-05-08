"""
이분탐색

최대로 건널 수 있는 인원 명수를 이분 탐색 타깃으로 두기


1. 다 밟을 수 있으면 동일하게 1씩 감소
2. 밟을 수 없으면 인원 수 줄이기
3. 밟을 수 있으면 인원 수 늘리기(갱신) -> 최대값 갱신

"""
def can_check(bridge, people, k):
    # 0 이하 구간이 연속되는 최대 횟수
    cnt = 0
    
    for stone in bridge:
        # 뛰어 넘을 수 없는 칸 : 남은 칸수 - 사람 수 음수면 못뛰어넘는 칸 +1
        if stone < people:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    
    return True       

def solution(stones, k):
    # 모든 디딤돌이 다 같은 숫자인 경우
    start, end = 0, max(stones)
    max_people = 0
    
    while start <= end:
        mid = (start + end) // 2
        # print('## people : ', mid)
        
        # 건널 수 있다는 뜻
        if can_check(stones.copy(), mid, k):
            max_people = max(max_people, mid) # 최대값 갱신
            start = mid + 1
            
        # 건널 수 없으면
        else:
            end = mid - 1
    
    return max_people