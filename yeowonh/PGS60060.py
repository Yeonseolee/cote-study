# 와일드카드 포함
# 알파벳은 노상관, 글자수는 1칸차지
from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    # 길이에 따라 나누어 저장
    # 접두사가 와일드카드인 경우 vs 접미사가 와일드카드인 경우
    arr = [[] for _ in range(10001)]
    reversed_arr = [[] for _ in range(10001)]
    
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])
    
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()
    
    for q in queries:
        # 접두사가 와일드카드인 경우 - 뒤에서부터 일치하는 거 찾기
        cnt = 0
        
        if q[0] == '?':
            # bisect left right
            '''
            a = [1,3,3,3,5]
            bisect_right(a,1) = 1
            bisect_left(a,1) = 0
            
            '''
            res = bisect_right(reversed_arr[len(q)], q[::-1].replace('?', 'a')) - bisect_left(reversed_arr[len(q)], q[::-1].replace('?', 'z'))
        else:
            res = bisect_right(arr[len(q)], q.replace('?', 'a')) - bisect_left(arr[len(q)], q.replace('?', 'z'))
            
        answer.append(abs(res))
    return answer