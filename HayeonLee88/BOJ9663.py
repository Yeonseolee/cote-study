n = int(input())
# graph[행] = 열
graph = [-1] * n

def check(x, y):

    # y열에 퀸이 있는지 확인
    if graph.count(y):
        return False
    # x행 이전 행에서 대각선 탐색
    for i in range(x):
        if graph[i] in [y - (x - i), y + (x - i)]:
            return False
    return True

answer = 0

def backtracking(i): # i행에 놓을 퀸의 위치를 찾는다
    global answer
    if i == n:
        if not graph.count(-1): # 퀸이 몇 개 놓였는지 세기
            answer += 1
        return
    for j in range(n):
        if not check(i, j): # i행 j열에 확인
            continue
        graph[i] = j
        backtracking(i + 1) # i + 1행에 놓을 퀸의 위치 backtracking
        graph[i] = -1

backtracking(0)
print(answer)