def function(seat_list):
    
    for row in range(5):
        for col in range(5):
            # 해당 자리가 P인 경우에만 진행
            if seat_list[row][col] != "P":
                continue
            
            # P가 우측 끝이 아니라면 우측부터 바라본다.
            if col<4:
                # 우측 바로 옆이 P 이면 실패
                if seat_list[row][col+1] == "P":
                    return 0
                #  빈자리 이면 그 우측과 밑을 체크
                if seat_list[row][col+1] == "O":
                    if col < 3 and seat_list[row][col+2] == "P":
                        return 0
                    if row < 4 and seat_list[row+1][col+1] == "P":
                        return 0
                # 파티션이 있을 경우, 다음 row로 이동한다.
                #if seat_list[row][col+1] == "X":
            
            # P가 맨 밑이 아니라면, 두번째 row로 이동한다.
            if row<4:
                # P 바로 밑이 P 이면 실패
                if seat_list[row+1][col] == "P":
                    return 0
                # P 바로 밑이 빈 자리 이면 그 아래와 옆을 확인
                if seat_list[row+1][col] == "O":
                    # 그 옆이 범위에 해당한다면
                    if col<4 and seat_list[row+1][col+1] == "P":
                        return 0
                    # 그 아래가 범위에 해당한다면
                    if row < 3 :
                        if seat_list[row+2][col] == "P":
                            return 0
                # P 아래가 파티션일 경우, 끝
    return 1

def solution(places):
    
    answer = []
    for room in places:
        result = function(room)
        answer.append(result)
    
    return answer

places = [["OOOOO", "OOOOO", "OOOOO", "OOOOP", "OOOPO"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
answer = solution(places)

print(answer)