"""
꽃 사지마라 그냥..
장미를 적어도 N개 구매하는데 필요한 최소 금액

A개를 B원에 팔고 / C개를 D원에

가성비 좋은걸 최대한 많이 사고, 마지막 더미는 a를 사는 것 vs b를 사는 것
-> 묶음 단위로 사기 때문에 1개 당 가격에 초점을 두면 안됨
-> 두 가개에서 팔고자하는 단위의 최소공배수 만큼의 장미를 살 때 더 저렴한 곳을 찾으면 됨

"""
import math

N, a_cnt, a_cost, b_cnt, b_cost = map(int, input().split())

# a묶음과 b묶음의 최소공배수 구하기
target = math.lcm(a_cnt, b_cnt)


# a를 더 가성비 좋은 것으로 놓기
if a_cost * b_cnt < b_cost * a_cnt:
    a_cost, b_cost = b_cost, a_cost
    a_cnt, b_cnt = b_cnt, a_cnt

min_cost = float('inf')

for a in range(b_cnt):
    b = math.ceil((N-a*a_cnt) / b_cnt)
    if b < 0:
        b = 0
        min_cost = min(min_cost, a * a_cost + b * b_cost)
        break

    min_cost = min(min_cost, a * a_cost + b * b_cost)

print(min_cost)

