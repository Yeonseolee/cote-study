"""
1. 절반으로 잘라서 계속 분할
2. result 배열에 추가

"""
import sys
from collections import Counter
sys.setrecursionlimit(10**5)

result = []

def check_color(paper):
    total = sum(sum(paper, []))
    if total == len(paper) * len(paper[0]):
        return 'B'
    elif total == 0:
        return 'W'
    else:
        return None
    

def recursive_cut(paper):
    global result
    paper_color = check_color(paper)

    # 4분할 하기
    if paper_color == None:
        r_mid = len(paper) // 2
        c_mid = len(paper[0])//2

        # 좌상단
        recursive_cut([row[:c_mid] for row in paper[:r_mid]])
        # 우상단
        recursive_cut([row[c_mid:] for row in paper[:r_mid]])
        # 좌하단
        recursive_cut([row[:c_mid] for row in paper[r_mid:]])
        # 우하단
        recursive_cut([row[c_mid:] for row in paper[r_mid:]])

    # 분할된 경우
    else:
        result.append(paper_color)

N = int(input())
paper = [[int(i) for i in sys.stdin.readline().split()] for r in range(N)]
recursive_cut(paper)
counter = Counter(result)
print(counter['W'])
print(counter['B'])