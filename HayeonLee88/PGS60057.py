def solution(s):
    length = len(s)
    answer = length
    for n in range(1, length // 2 + 1):
        tmp = 0 # 압출된 문자열 길이
        prev = ''
        cnt = 1 # 같은 문자열이 반복되는 횟수
        for i in range(0, (length // n) * n, n):
            if prev == s[i: i + n]: # n 단위로 자른 문자열이 이전과 같을 때
                cnt += 1
            else: # n 단위로 자른 문자열이 이전과 다를 때
                if cnt > 1: # 이전 문자열이 압축된 문자열이었을 때
                    tmp += len(str(cnt))
                cnt = 1
                prev = s[i: i + n]
                tmp += n
        if cnt > 1: # 압축된 문자열로 끝났을 때
            tmp += len(str(cnt))
        tmp += length % n # 문자열을 n개의 단위로 나눈 후 남은 문자 수
        answer = min(answer, tmp)

    return answer
