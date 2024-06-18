'''
알파벳 소문자로 이루어진 N개의 단어 정렬하기

조건 
1. 길이가 짧은 것 부터
2. 길이가 같으면 사전 순으로
3. 중복된 단어는 하나만 남기고 제거하기

풀이 
- set()으로 입력 받기
- 사전 순으로 정렬하기
- 길이 순으로 정렬하기
'''
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

words = set(input() for _ in range(n))

sorted_words = sorted(words)
sorted_words = sorted(sorted_words, key=lambda x: len(x))

print(*sorted_words, sep='\n')


'''
1년 전 풀이

import sys
n = int(input())
words = list({sys.stdin.readline().rstrip() for _ in range(n)})
words.sort()
words.sort(key=lambda x: len(x))
for word in words:
    print(word)
    
'''