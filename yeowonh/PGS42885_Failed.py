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
    
    while people:
        boat = 0
        # 무거운 사람부터
        boat += people.pop(0)
        
        # 가벼운 사람?
        if people and boat + people[-1] <= limit:
            boat += people.pop()
        
        answer += 1
        
    return answer