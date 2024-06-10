def can_distribute(snacks, nephew, length):
    # 주어진 길이로 나눈 과자의 총 개수를 계산하는 함수
    count = 0
    for snack in snacks:
        # 각 과자를 length로 나눈 몫을 총 개수에 추가
        count += snack // length
        # 이미 필요한 개수를 충족한 경우, 더 이상 계산할 필요 없이 참 반환
        if count >= nephew:
            return True
    # 필요한 개수를 충족하지 못한 경우 거짓 반환
    return False

def find_max_length(nephew, snacks):
    # 이진 탐색을 사용하여 과자를 나눠줄 수 있는 최대 길이를 찾는 함수
    left, right = 1, max(snacks)  # 검색 범위를 설정 (최소 1, 최대 과자 길이)
    ans = 0  # 최대 길이를 저장할 변수
    while left <= right:
        mid = (left + right) // 2  # 중간점을 찾음
        # 만약 현재 중간 길이로 모든 조카에게 과자를 충분히 나눠줄 수 있다면
        if can_distribute(snacks, nephew, mid):
            ans = mid  # 답을 현재 중간 길이로 갱신
            left = mid + 1  # 가능한 길이를 늘려 더 긴 길이를 탐색
        else:
            right = mid - 1  # 길이가 너무 길어 충분한 개수를 나눠줄 수 없으므로 길이를 줄임
    return ans  # 최대 길이 반환

# 입력 받기
nephew, _ = map(int, input().split())
snacks = list(map(int, input().split()))

# 최대 길이 계산 및 출력
max_length = find_max_length(nephew, snacks)
print(max_length)
