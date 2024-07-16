'''
8:44~
한 톱니바퀴를 n반향으로 돌릴 때 옆의 톱니바퀴의 맞다은 부분이 서로 다른 극을 가지고 있다면 반대반향으로 회전한다.


N극: 0, S극: 1
시계 방향: 1, 반시계 방향: -1
12시 방향: index 0

1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점

solution:
  deque의 rotate함수를 사용하여 톱니바퀴를 회전시킨다.

  맟닿은 부분은 deque의 2번과 -3번 인덱스, 
  톱니바퀴 번호    1   2   3   4
  톱니 번호    (2 -2) (2 -2) (2 -2) 

  state에 맞닿은 부분의 합을 저장하여 해당 값이 1이면 맞닿은 톱니를 반대로 회전한다.
'''
import sys
from collections import deque

input = lambda:sys.stdin.readline().rstrip()
wheels = {}
for i in range(1, 5):
    wheels[i] = deque(map(int, list(input())))

state = []
def rotate(start, end, dir1, dir2): 
    '''
    start, end: 번호 내를 탐색
    dir1: -1 이면 왼쪽 1이면 오른쪽 방향 톱니 탐색
    dir2: 톱니가 돌아갈 방향
    '''
    global state
    d = dir2 # 시계, 반시계 방향
    for i in range(start, end, dir1):
        d *= -1
        if dir1 == 1:
            if state[i -1] == 1:
                wheels[i].rotate(d)
            else:
                break
        else:
            if state[i] == 1:
               wheels[i].rotate(d)
            else:
                break
        
n = int(input())
answer = 0
for i in range(n):
    state = [-1, wheels[1][2] + wheels[2][-2], wheels[2][2] + wheels[3][-2], wheels[3][2] + wheels[4][-2]]
    num, dir = map(int, input().split())
    wheels[num].rotate(dir)
    rotate(num -1, 0, -1, dir) # 왼쪽 방향 탐색
    rotate(num + 1, 5, 1, dir) # 오른쪽 방향 탐색

for j in range(4):
     if wheels[j + 1][0] == 1:
        answer += 2 ** j
                   
print(answer)