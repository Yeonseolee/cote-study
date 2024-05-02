import sys

input = lambda: sys.stdin.readline().rstrip()

K, L = map(int, input().split())
deagi = {input(): i for i in range(L)} # key-value : ('학번' : '대기번호 들어온 순서')
# 입력만으로도 저절로 중복으로 들어온 학번은 나중에 들어온 순서로 배치됩니다
# python의 dictionary 자료형은 key값의 중복을 허용하지 않기 때문에.. 중복이더라도 나중에 들어온 대기번호 순서가 마지막 value 값으로 저장됩니다.
ans = sorted(deagi.items(), key=lambda x : x[1])

for i, elems in enumerate(ans):
    if i >= K:
        break
    print(elems[0])


    
