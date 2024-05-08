# 길이 N, 합 S
n, s = map(int, input().split())
# 수열
numbers = list(map(int, input().split()))

total = 0 # 맨 처음 인덱스값
min_len = n + 1 # s 최대값

low = 0; high = 0

# 원소 끝에서 달성되는 경우
while True:
    # print(f'## low : {low}, high : {high}')
    # 매번 sum 계산하지 말고 total에다가 더하고 빼기
    # 합이 아직 작을 경우 -> high 범위 늘리기
    if total >= s:
        min_len = min(min_len, high-low)
        total -= numbers[low]
        low += 1
    # 끝에 도달하면 break
    elif high == n:
        break
    # 합이 같거나 크면 -> low 범위 좁히기, 더 작은 범위 찾아보기
    else:
        total += numbers[high]
        high += 1
    # print('## total : ', total)

# 끝까지 돌았는데도 안나옴 (high가 n에 도달) -> 결과 없는 것
if min_len == n+1:
    print(0)
else:
    print(min_len)