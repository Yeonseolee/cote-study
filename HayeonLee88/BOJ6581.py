import sys

input = lambda: sys.stdin.readlines()
tmp = -1 # 한 줄의 글자 길이
words = [] # 입력된 전체 단어 리스트

lines = input()
for line in lines:
    words += line.split()

output = [] # 한 줄에 출력할 단어 리스트
for word in words:
    if word == "<br>": # output 리스트 출력 후 개행
        print(" ".join(output))
        output = []
        tmp = -1 # 초기화
        continue
    elif word == "<hr>":
        if output: # output 리스트가 비어있지 않다면 출력 후 개행
            print(" ".join(output))
        print("-" * 80) # - * 80 출력 후 개행
        output = []
        tmp = -1 # 초기화
        continue
    tmp += (len(word) + 1) # 단어 길이 + 공백문자

    if tmp > 80: # output 리스트 출력 후 개행
        print(" ".join(output))
        output = [word]
        tmp = len(word)
        continue
    output.append(word)

if output: # for문이 끝난 후 남은 단어 출력
    print(" ".join(output))