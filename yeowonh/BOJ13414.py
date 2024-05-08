"""
1. 들어온 순서대로 dict에 value로 넣기
2. 이미 있을 경우 갱신
"""
import sys

def solution(k, l):
    students = [sys.stdin.readline().strip() for i in range(l)]
    student_dict = {}

    for i, student in enumerate(students):
        student_dict[student] = i

    # print('#' * 10)
    # print(students)
    
    student_dict = sorted(student_dict.items(), key=lambda x: x[1])
    # print(student_dict)
    for student in student_dict[:k]:
        print(student[0])

    return


k, l = map(int, sys.stdin.readline().split())
solution(k, l)