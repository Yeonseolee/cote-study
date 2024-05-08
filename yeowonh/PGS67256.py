def solution(numbers, hand):
    # 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작
    # 1. 엄지는 상하좌우 거리 1
    # 2. 왼쪽 열의 3개 1, 4, 7은 ㅇ왼손 엄지
    # 3. 오른 열의 3개 369는 오른엄지
    # 4. 가운데 열은 2580을 입력할 때는 현재 위치에서 더 가까운 엄지 사용
    # 4-1. 거리 같다면 오른손잡이는 오른손, 왼손잡이는 왼손
    
    # 움직인 현재 위치 저장해야 함
    # 키패드의 좌표를 dictionary로 저장
    # dx, dy로 상하좌우 조작 / 현재 위치와의 차이 거리로 따지기
    '''
    1   2   3
    4   5   6
    7   8   9
    *   0   #
    
    '''
    keypad = {"1" : [0,0], "2" : [0,1], "3" : [0,2], 
              "4" : [1,0], "5" : [1,1], "6" : [1,2], 
              "7" : [2,0], "8" : [2,1], "9" : [2,2],
              "*" : [3,0], "0" : [3,1], "#" : [3,2]}
    
    lh = [3, 0]; rh = [3, 2] # 시작 위치
    
    answer = ''
    
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            # 왼손이 이동
            new_dir = keypad[str(num)]
            answer += 'L'
            lh = new_dir
        elif num == 3 or num == 6 or num == 9:
            # 오른손이 이동
            new_dir = keypad[str(num)]
            answer += 'R'
            rh = new_dir
        else:
            # 왼손, 오른손과의 거리 계산
            new_dir = keypad[str(num)]
            lh_dis = abs(lh[0]-new_dir[0]) + abs(lh[1]-new_dir[1])
            rh_dis = abs(rh[0]-new_dir[0]) + abs(rh[1]-new_dir[1])
            
            # 왼손 거리가 작을 경우
            if lh_dis < rh_dis:
                answer += 'L'
                lh = new_dir
            elif lh_dis > rh_dis:
                answer += 'R'
                rh = new_dir
            else:
                if hand == 'left':
                    answer += 'L'
                    lh = new_dir
                else:
                    answer += 'R'
                    rh = new_dir
            
    return answer