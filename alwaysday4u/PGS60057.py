def solution(s):
    ans = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2 + 1):
        cand = ''
        cnt = 1
        pttn = s[:i]
        
        for j in range(i, len(s), i):
            if pttn == s[j:i+j]: cnt+=1
            else:
                if cnt == 1: cand += pttn
                else: cand += str(cnt) + pttn
                pttn = s[j:i+j]
                cnt = 1
        
        if cnt != 1: cand += str(cnt) + pttn
        else: cand += pttn

        ans.append(len(cand))
    
    return min(ans)
