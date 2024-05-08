'''
부분합 중에서 그 합이 S 이상이 되는 것 중 가장 짧은 것의 길이
순서를 바꾸면 안된다

합이 15 이상
5 1 3 5 10 7 4 9 2 8

시간 복잡도 상 모든 것을 탐색하는 것은 당연히 안될거고..
인덱스를 유지하면서도 탐색하는 방법? -> 투 포인터

'''
# 길이 N, 합 S
n, s = map(int, input().split())
# 수열
numbers = list(map(int, input().split()))

total = numbers[0] # 맨 처음 인덱스값
min_len = 10**8 + 1 # s 최대값

low = 0; high = 1

# max가 나오는 경우를 우선적으로 찾기?
# 이분탐색
while low <= high and high < n:
    # print(f'## low : {low}, high : {high}')
    # 매번 sum 계산하지 말고 total에다가 더하고 빼기
    # 합이 아직 작을 경우 -> high 범위 늘리기
    if total < s:
        total += numbers[high]
        high += 1
    # 합이 같거나 크면 -> low 범위 좁히기, 더 작은 범위 찾아보기
    else:
        min_len = min(min_len, high-low)
        total -= numbers[low]
        low += 1
    # print('## total : ', total)

# 끝까지 돌았는데도 안나옴 (high가 n에 도달) -> 결과 없는 것
if min_len == len(numbers)+1:
    print(0)
else:
    print(min_len)

"""
70% 까지 진행되었으나 이후 “틀렸습니다” 떴음

반례:
10 10
1 1 1 1 1 1 1 1 1 10

맨 끝의 원소가 제대로 안들어감 (high<n 조건문에 걸려서 탐색 중단됨)
"""