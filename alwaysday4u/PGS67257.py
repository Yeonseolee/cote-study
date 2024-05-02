import math

def distance(edge1, edge2):
    return abs(edge2[0] - edge1[0]) + abs(edge2[1] - edge1[1])

def solution(numbers, hand):
    pos = {
        1: (0,3), 2: (1,3), 3: (2,3),
        4: (0,2), 5: (1,2), 6: (2,2),
        7: (0,1), 8: (1,1), 9: (2,1),
        '*': (0,0), 0: (1,0), '#': (2,0)
    }
    left_pos = '*'
    right_pos = '#'
    answer = []
    
    for num in numbers:
        if num in [1, 4, 7]:
            left_pos = num
            answer.append('L')
        if num in [3, 6, 9]:
            right_pos = num
            answer.append('R')
        if num in [2, 5, 8, 0]:
            left_distance = distance(pos[left_pos], pos[num])
            right_distance = distance(pos[right_pos], pos[num])
            if left_distance < right_distance:
                left_pos = num
                answer.append('L')
            if left_distance > right_distance:
                right_pos = num
                answer.append('R')
            if left_distance == right_distance:
                if hand == 'left':
                    left_pos = num
                    answer.append('L')
                if hand == 'right':
                    right_pos = num
                    answer.append('R')
    
    return ''.join(answer)
