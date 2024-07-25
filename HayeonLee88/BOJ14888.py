from itertools import permutations

n = int(input())
sequence = list(map(int, input().split()))
operator_cnt = list(map(int, input().split()))
operators = ['+'] * operator_cnt[0] + ['-'] * operator_cnt[1] + ['*'] * operator_cnt[2] + ['//'] * operator_cnt[3]
operator_seq = set(permutations(operators, n - 1))
answer = []

for ops in operator_seq:
    tmp = sequence[0]
    for i in range(n-1):
        op = ops[i]
        if op == '+':
            tmp += sequence[i+1]
        elif op == '-':
            tmp -= sequence[i + 1]
        elif op == '*':
            tmp *= sequence[i + 1]
        else:
            if tmp < 0 :
                tmp = - (- tmp // sequence[i + 1])
            else:
                tmp //= sequence[i + 1]
    answer.append(tmp)

print(max(answer))
print(min(answer))

