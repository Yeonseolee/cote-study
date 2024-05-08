# 그려진 선들의 총 길이
"""
1 3
2 5 -> 1 5
3 5
6 7 -> 1

"""
def solution(N):

    lines = []

    for _ in range(N):
        x, y = map(int, input().split())
        lines.append([x, y])
    
    # 정렬하기
    lines.sort()

    total = 0
    prev_x, prev_y = lines[0]

    for idx in range(1, len(lines)):
        x, y = lines[idx]
        # 시작점과 끝 좌표가 겹친다면
        if x < prev_y:
            prev_y = max(y, prev_y)
        else:
            total += prev_y - prev_x
            prev_x, prev_y = x, y

    total += prev_y - prev_x

    return total


N = int(input())
print(solution(N))