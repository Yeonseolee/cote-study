"""
N개의 좌표 압축.. 문제가 잘 이해가 안가네
오름차순 정렬하고 인덱스인 듯?? -- 중복 제거 필요
"""
import sys

n = int(input())
coor = list(map(int,sys.stdin.readline().strip().split()))

sorted_coor = sorted(list(set(coor)))
# 정렬 인덱스 딕셔너리 형태로 만들어주기 {-10 : 0, -9 : 1}
dictList = dict(zip(sorted_coor, list(range(len(sorted_coor)))))

for c in coor:
    print(dictList[c], end=' ')
