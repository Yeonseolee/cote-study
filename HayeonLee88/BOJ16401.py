import sys
input = lambda:sys.stdin.readline().rstrip()

m, n = map(int, input().split())
snacks = list(map(int, input().split()))
snacks.sort()

start = 1
end = snacks[-1]
answer = 0
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for snack in snacks:
        tmp += snack // mid
    if tmp < m : # 과자 개수가 모자르다면, 더 작게 나누기
        end = mid - 1
    elif tmp >= m: # 과자 개수가 더 많거나 같다면, 길이를 더 길게 나눠 최대 길이 구하기
        answer = mid
        start = mid + 1

print(answer)