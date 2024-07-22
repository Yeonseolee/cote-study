'''
12:01~12:19

올바른 괄호의 조건
1. 짝수여야 한다.
2. 열림 괄호부터 시작한다.
3. 닫힘 괄호는 가장 최근의 열림 괄호의 모양과 일치해야 한다.
4. 모든 열림 괄호와 짝이 맞는 닫힘 괄호가 존재해야 한다.

solution
- 괄호의 개수가 짝수인지 체크한다.
- stack : 열림 괄호를 담는 스택
- 닫힘 괄호가 나오면 stack.pop() 하여 모양의 일치를 확인한다.
- s를 다 돌았을 때 if not stack 이면  +1
'''

def solution(s):
    answer = 0
    stack = []
    n = len(s)
    
    dic = {'(': ')', '[': ']', '{': '}'}
    if n % 2 != 0:
        return 0
    
    for _ in range(n):
        check = True
        for x in s:
            if x in ['(', '[', '{']: # 열림 괄호라면
                stack.append(x)
            else:
                if stack: 
                    prev = stack.pop()
                    if dic[prev] != x: # 최근 열림 괄호와 현재 닫힘 괄호의 모양이 다를 때
                        check = False
                        break
                else: # 열림 괄호와 닫힘 괄호의 개수가 안 맞을 때
                    check = False
                    break
        if check:
            answer += 1
        s = s[1:] + s[0]
                
    return answer
######################################################
# 1년 전 풀이

# left = 1, right = -1
dic = {'(': [1, ')'], ')': [-1, '('], '[': [1, ']'], ']': [-1, '['], 
       '{': [1, '}'], '}': [-1, "{"]}

def check_str(string):
    if len(string) % 2 == 1: # 괄호 짝이 안 맞으면
        return False
    pos, checked_str = 0, []

    for s in string:
        d_pos, d_s = dic[s] # 다음 왼/오, 괄호의 짝 모양
        n_pos = pos + d_pos

        if n_pos < 0: # 닫힘 괄호가 더 많을 때
            return False
        elif d_pos == -1 and d_s != checked_str[-1] : # 열림 괄호 순서와 안 맞는 닫힘 괄호가 오면
            return False
        if d_pos == -1: # 닫힘 괄호가 오면 열림 괄호 제거
            checked_str.pop()
        else: # 열림 괄호가 오면 체크한 괄호 리스트에 추가
            checked_str.append(s)
        pos = n_pos # 괄호 방향의 수를 바꿈
    return True
    
def solution(s):
    answer = 0
    length = len(s)
    for i in range(length):
        new_str = s[1:] + s[0]
        if check_str(new_str):
            answer += 1
        s = new_str
    return answer
######################################################

