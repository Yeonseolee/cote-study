from bisect import bisect_right, bisect_left

def solution(words, queries):
    # 단어를 같은 길이끼리 함께 저장할 리스트: data, reversed_data
    data = [[] for _ in range(10001)]
    reversed_data = [[] for _ in range(10001)] # 접두사 키워드를 위해 단어를 뒤집어 저장하는 리스트
    
    for word in words: 
        data[len(word)].append(word)
        reversed_data[len(word)].append(word[::-1])
        
    for i in range(10001): # 길이가 같은 단어들을 알파벳 순으로 오름차순 정렬한다.
        data[i].sort()
        reversed_data[i].sort()
    
    answer = []
    
    for q in queries:
        if q[0] == '?': # 접두사일 경우
            # 키워드를 뒤집고 ?를 a/z로 바꾼 뒤 
            # 키워드의 길이와 같은 단어들 사이에 들어갈 첫/끝 위치를 찾는다. 
            first = bisect_left(reversed_data[len(q)], q[::-1].replace('?', 'a')) 
            last = bisect_right(reversed_data[len(q)], q[::-1].replace('?', 'z'))
        else: # 접미사일 경우
            # 접미사를 모두 a/z로 바꾼 뒤 
            # 키워드의 길이와 같은 단어들 사이에 들어갈 첫/끝 위치를 찾는다. 
            first = bisect_left(data[len(q)], q.replace('?', 'a'))
            last = bisect_right(data[len(q)], q.replace('?', 'z'))
        answer.append(last-first) # 끝 위치 - 첫 위치 = 키워드와 일치하는 단어 개수
                                
    return answer