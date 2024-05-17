from itertools import permutations

n, m = map(int, input().split())

# 순열로 풀기
####################################################

arrays = list(permutations(range(1, n + 1), m))

for array in arrays:
    for x in array:
        print(x, end=' ')
    print()

# 벡트랙킹으로 풀기
#####################################################

nums = [i for i in range(1, n + 1)]
visited = [False] * (n + 1)
answer = [0] * m

def backtracking(i):
    if i == m:
        print(*answer)
        return
    for num in nums:
        if visited[num]: # 이미 방문한 숫자라면 continue
            continue
        answer[i] = num
        visited[num] = True
        backtracking(i + 1) # i번째 이후의 숫자를 담기 위해 재귀 호출 
        visited[num] = False # i번째 이후에 num이 들어가기 위해 False로 바꾸기

backtracking(0)
