'''
4:30~50

[이분탐색]
길이가 제각각인 K개의 랜선을 길이가 같은 N개의 랜선으로 만들기
N개 이상이 만들어지도록 할 때 만들 수 있는 랜선의 최대 길이
K: 랜선의 개수 (1 이상 10,000 이하)
N: 필요한 랜선의 개수 (1 이상 1,000,000 이하)

최대 길이 = K개의 랜선 중 최대 길이
'''
import sys
input = lambda:sys.stdin.readline().rstrip()

k, n = map(int, input().split())
wires = [int(input()) for _ in range(k)]
wires.sort(reverse = True) # 랜선의 길이를 내림차순 정렬

start = 1
end = wires[0] # 가장 짧은 길이의 랜선
answer = 1

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    check = False # 랜선을 잘랐을 때 N개를 넘는지 체크
    for wire in wires:
        tmp += (wire // mid)
        if tmp >= n: # N개를 넘을 때
            answer = max(answer, mid) # 최대값을 정답으로
            check = True
            start = mid + 1
            break
    if not check:
        end = mid - 1

print(answer)
