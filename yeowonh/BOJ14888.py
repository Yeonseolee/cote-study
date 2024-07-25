"""
수와 수 사이에 연산자
연산은 무조건 앞에서부터

결과의 최대 최소값을 산출하기

op_list가 사용 가능한 연산자 수로 들어옴 -> 그러니까 모든 순열을 조사해봐야 한다는 이야기

... 이렇게 해도 풀리네
백트래킹이란 대체 뭘까
"""
from itertools import permutations

N = int(input())
num_list = list(map(int, input().split()))
op_list = list(map(int, input().split()))
op_dict = {0:'+', 1:'-', 2:"*", 3:"//"}
op_list_ch = []

for idx, x in enumerate(op_list):
    op_list_ch += [op_dict[idx]] * x

op_list_ch = list(permutations(op_list_ch, N-1))

min_value = 10**9; max_value = -10**9

# 모든 경우의 수 돌면서 인덱스 옮기기
for op_list in op_list_ch:
    cur_value = num_list[0]
    idx = 1
    for op in op_list:
        if op == '+':
            cur_value += num_list[idx]

        elif op == '-':
            cur_value -= num_list[idx]
        
        elif op == '*':
            cur_value *= num_list[idx]
        # 여기서 문제 발생
        else:
            if cur_value < 0:
                cur_value = abs(cur_value)
                cur_value //= num_list[idx]
                cur_value = -cur_value
            else:
                cur_value //= num_list[idx]
        
        idx += 1
    
    min_value = min(min_value, cur_value)
    max_value = max(max_value, cur_value)

    # if cur_value < min_value:
    #     min_value = min(min_value, cur_value)
    #     min_op = op_list
    
    # if cur_value > max_value:
    #     max_value = max(max_value, cur_value)
    #     max_op = op_list

print(max_value)
print(min_value)
# print(f"## 최대값 : {max_value}, ## 연산 : {max_op}")
# print(f"## 최대값 : {min_value}, ## 연산 : {min_op}")