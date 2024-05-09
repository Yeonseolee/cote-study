
"""
몇 개 단위로 압축할 지 순회하기
제일 앞부터 정해진 길이만큼 잘라야 함
"""

def solution(s):
    # 맨 처음에는 문자열 원래 길이 (압축 안됐을 때)
    answer = len(s)
    
    # 1~n-1 길이로 자르기
    for length in range(1, len(s)):
        comp_str = ''
        word_dict = {}
        
        # 문자열 맨 처음부터 순회하면서 키 등록
        for idx in range(0, len(s), length):
            new_str = s[idx:idx+length]
            
            # 다른 문자열 나올 경우에는 comp_str에 추가하고 딕셔너리에서 키 삭제
            if len(word_dict.keys()) == 0: # 맨 처음
                word_dict[new_str] = 1
                
            elif new_str not in word_dict:
                key = list(word_dict.keys())[0]; value = word_dict[key]
                
                if value != 1:
                    comp_str += str(value) + key
                else:
                    comp_str += key
                    
                del word_dict[key] # 삭제
                word_dict[new_str] = 1 # 새로 등록
                
            else:
                word_dict[new_str] += 1
                
        # 남아있는 거 넣기
        if len(word_dict.keys()) != 0:
            key = list(word_dict.keys())[0]; value = word_dict[key]
            
            if value != 1:
                comp_str += str(value) + key
            else:
                comp_str += key
        
        answer = min(answer, len(comp_str))
    
    return answer