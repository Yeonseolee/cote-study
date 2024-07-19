"""
**2명** / 무게 제한
[70kg, 50kg, 80kg, 50kg]

구명보트 최대한 적게 사용하기
가벼운 사람 + 무거운 사람
50 50 70 80
50
50
70
80


80 70 50 50
80
70
50
50

-> 무거운 사람부터 태워야 함

"""
def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    start, end = 0, len(people) - 1
    
    # 리스트 원소 자체를 pop하면 시간 초과 발생 -> 투 포인터 방식!
    while start <= end:
        
        # 사람 1명은 무조건 태울 수 있으므로, 가벼운 사람을 추가로 태울 수 있는지만 체크
        if people[start] + people[end] <= limit:
            end -= 1
        
        start += 1
        answer += 1
    
    return answer