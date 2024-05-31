"""
과자 최대 길이를 이분탐색 target으로 두기
"""
m, n = map(int, input().split())
cookies = list(map(int, input().split()))
cookies.sort()

start, end = 1, cookies[-1]
target = 0 # 안될경우 0 출력


while start <= end:
    mid = (start + end) // 2

    total = 0

    # m명한테 줄 수 있는지 아닌지도 판단해야 함
    # mid 값을 기준으로 나눠줄 수 있는 개수 구하기
    for c in cookies:
        # 10 // 7 = 1
        if c >= mid:
            total += c // mid

    # 범위 늘리기
    if total >= m:
        target = mid
        start = mid + 1
    else:
        end = mid - 1

print(target)