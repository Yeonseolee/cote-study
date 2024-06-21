"""
값을 최소로 만들기 -> 괄호를 마음대로 쳐서 만들기

ex. 55-50+40

55
-
50+40

70+20-30-40

10+20
-
30
-
40

- 기준 split하고 +인것만 전부 더한다면?
"""

op_str = input()
num_list = op_str.split('-')

for idx, num in enumerate(num_list):
    num_total = num.split('+')
    if len(num_total) == 1:
        num_list[idx] = int(num)
    else:
        num_list[idx] = sum(list(map(int, num_total)))

answer = num_list[0]

for i in range(1, len(num_list)):
    answer -= num_list[i]

print(answer)