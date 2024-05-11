def solution(s):
    ans = []  # 압축 후 문자열 길이를 저장할 리스트
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)//2 + 1):
        cand = ''  # 현재 압축 단위로 압축한 결과를 저장할 문자열
        cnt = 1  # 반복되는 패턴의 수
        pttn = s[:i]  # 현재 패턴
        
        # i 간격으로 문자열을 순회하면서 패턴과 비교
        for j in range(i, len(s), i):
            if pttn == s[j:i+j]:
                cnt += 1
            else:
                if cnt == 1: cand += pttn
                else: cand += str(cnt) + pttn
                pttn = s[j:i+j]
                cnt = 1
        
        # 마지막 패턴 추가 처리
        if cnt != 1: cand += str(cnt) + pttn
        else: cand += pttn
        
        # 현재 압축 길이를 결과 리스트에 추가
        ans.append(len(cand))
    
    # 가능한 모든 압축 길이 중 가장 짧은 길이 반환
    return min(ans)
