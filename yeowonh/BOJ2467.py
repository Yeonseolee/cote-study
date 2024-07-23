"""
큰 범위의 정수 -> 단순 반복문 대신 투포인터로!

**입력은 오름차순**
특성값의 합이 0에 가장 가깝도록 -> 출력은 오름차순 (입력에 주어진대로)

"""

n = int(input())
liquids = list(map(int, input().split()))
answer = 2000000001

start, end = 0, n-1
s, e = start, end

while start < end:
    # 0에 가까울 때마다 갱신
    if abs(liquids[start] + liquids[end]) < answer:
        answer = abs(liquids[start] + liquids[end])
        s, e = start, end

    # 값이 0보다 작으면 start + 1
    if liquids[start] + liquids[end] < 0:
        start += 1
    # 값이 0보다 크면 end - 1
    else:
        end -= 1
    

print(liquids[s], liquids[e])