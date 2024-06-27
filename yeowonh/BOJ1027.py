"""
빌딩 N개가 있음
가장 많은 고층 빌딩이 보이는 빌딩
두 지붕을 잇는 선분이 A와 B를 제외한 다른 빌딩을 지나거나 접하지 않아야 함

오른쪽 -> 기울기가 앞선 건물보다 크면 카운트하기
왼쪽 -> 기울기가 앞선 건물보다 작으면 카운트하기
"""

def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

n = int(input())
heights = list(map(int, input().split()))
max_building_cnt = 0

for i1, h in enumerate(heights):
    cnt = 0
    previous = None
    # 왼쪽 빌딩들 확인
    for i2 in range(i1-1, -1, -1):
        if i2 == -1: break
        if previous == None or slope(i1, h, i2, heights[i2]) < previous:
            previous = slope(i1, h, i2, heights[i2])
            cnt += 1
    
    previous = None
    # 오른쪽 빌딩들 확인
    for i3 in range(i1+1, n):
        if i3 == n: break
        if previous == None or slope(i1, h, i3, heights[i3]) > previous:
            previous = slope(i1, h, i3, heights[i3])
            cnt += 1
    
    max_building_cnt = max(cnt, max_building_cnt)
            
print(max_building_cnt)