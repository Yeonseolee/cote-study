'''
N: (4 ≤ N ≤ 20, N은 짝수) 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 나눈다.
능력치 S_ij: i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치
팀의 능력치: 팀에 속한 모든 쌍의 능력치 Sij의 합

스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소

풀이
- 백트래킹을 이용하여 N개 중 N/2개를 고른다.
- 한 팀의 능력치를 구한다. 다른 팀의 능력치를 구한다. 두 능력치의 차를 구한다.

최대 20C10
'''
import sys
INF = 1e9

sys.setrecursionlimit(100000)
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = n // 2
array = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n 

def calc_stat(x):
    a = x
    b = list(range(n))

    for i in a:
        b.remove(i)
    ab = list(zip(a, b))

    a_hap= 0
    b_hap = 0
    for a_i, b_i  in ab:
        for a_j, b_j in ab:
            a_hap += array[a_i][a_j]
            b_hap += array[b_i][b_j]

    return abs(a_hap - b_hap)

answer = INF 
def backtracking(idx, cnt, state):
    global answer
    if cnt == m:
        tmp = calc_stat(state)
        if tmp == 0:
            print(0)
            exit()
        answer = min(answer, tmp)
        return
    
    else:
        for i in range(idx, n):
            if not visited[i]:
                state.append(i)
                visited[i] = True
                backtracking(i, cnt + 1, state)
                state.pop()
                visited[i] = False

backtracking(0, 0, [])
print(answer)