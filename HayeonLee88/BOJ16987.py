'''
계란으로 계란치기: 각 계란의 내구도는 상대 계란의 무게만큼 깎임.
    내구도가 0 이하가 되는 순간 계란이 깨짐.
일렬로 놓인 계란에 대해 왼쪽부터 차례대로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨는 문제

1. 가장 왼쪽의 계란을 든다.
2. 손에 들고 있는 계란으로 깨지지 않은 다른 계란 중에서 하나를 친다. 
    단, 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다. 
    이후 손에 든 계란을 원래 자리에 내려놓고 3번 과정을 진행한다.
3. 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정을 다시 진행한다. 
    단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란을 치는 과정을 종료한다.

계란의 수 =  N (1 ≤ N ≤ 8)
계란의 내구도 =  Si(1 ≤ Si ≤ 300)
계란의 무게 = Wi(1 ≤ Wi ≤ 300)

풀이
- 백트래킹 이용
- 왼쪽에 있는 계란으로 아직 안깨진 계란을 친다
- 가장 오른쪽까지 오거나 모든 계란이 깨졌다면 종료
'''
import sys

sys.setrecursionlimit(100000)
n = int(input())

eggs = [list(map(int, input().split())) for _ in range(n)]

answer = [0]
def backtracking(idx, cnt):
    if cnt == n: # 모든 계란이 깨졌다면
        print(n)
        exit()

    if idx == n: # 가장 오른쪽 계란까지 왔다면
        answer.append(cnt)
        return
    
    if eggs[idx][0] <= 0: # 현재 손에 든 계란이 깨졌다면
        backtracking(idx + 1, cnt)
    
    else: # 계란치기
        for i in range(n):
            tmp = cnt
            if i == idx: # 현재 계란 제외
                continue
            if eggs[i][0] > 0: # 안깨진 계란치기
                eggs[idx][0] -= eggs[i][1]
                eggs[i][0] -= eggs[idx][1]
                if eggs[idx][0] <= 0:
                    tmp += 1
                if eggs[i][0] <= 0: 
                    tmp += 1
                backtracking(idx + 1, tmp) # 다음 계란으로 이동
                eggs[idx][0] += eggs[i][1]
                eggs[i][0] += eggs[idx][1]
            else: # 깨진 계란 넘어가기
                backtracking(idx + 1, tmp)

backtracking(0, 0)
print(max(answer))