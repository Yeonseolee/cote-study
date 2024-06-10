'''
1. 옷 종류 중 한 가지 입을 수 있음.
2. 착용한 의상의 일부가 겹쳐도 ㄱㅊ음. -> 부분 집합 ok
3. 하루에 최소 한 개의 옷을 입는다.

풀이
(A 종류 + 1) * (B 종류 + 1) * ... * (Z 종류 + 1) - 1(아무 옷도 안입은 경우 빼기)
'''
from functools import reduce

def solution(clothes):
    dict_ = dict()
    
    for name, category in clothes:
        try:
            dict_[category] += 1
        except KeyError: # 처음 나온 종류라면
            dict_[category] = 2
            
    return reduce(lambda x, y: x * y ,dict_.values()) - 1


'''
1년 전 풀이

from functools import reduce

def solution(clothes):
    closet = {}
    for clothe in clothes:
        type = clothe[1]
        if type in closet.keys():
            closet[type] += 1
        else:
            closet[type] = 2
    answer = reduce(lambda x, y: x * y, closet.values()) - 1
    return answer
'''