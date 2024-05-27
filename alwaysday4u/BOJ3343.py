import math

n, a, a_price, b, b_price = map(int, input().split())
ans = float('inf')

if a/a_price < b/b_price:
    a, a_price, b, b_price = b, b_price, a, a_price

for b_cnt in range(a):
    a_cnt = math.ceil((n-b_cnt*b)/a)
    temp = False
    
    if a_cnt < 0:
        a_cnt = 0
        temp = True
        
    ans = min(ans, a_cnt*a_price + b_cnt*b_price)
