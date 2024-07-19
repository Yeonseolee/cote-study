"""
Knuth-Morris-Pratt (KMP) 알고리즘?
부분 문자열 검색에서 시간 복잡도를 O(n + m)으로 줄일 수 있는 방법
"""

# KMP 알고리즘을 위한 부분 일치 테이블을 생성하는 함수
"""
만약 pidx번째 글자와 idx 글자가 같다면, 패턴 일치 길이가 1칸 늘어난 것이므로 pidx를 1 증가시키고 그 값을 접두사-접미사 테이블의 idx번째에 저장한다.
pidx번째 글자와 idx 글자가 같지 않다면, 현재 문자열에선 동일 접두사-접미사가 존재하지 않다는 뜻이므로 접두사 포인터인 pidx는 이전으로(=동일 접두사-접미사가 존재했던 문자열) 되돌아간다으로 되돌아간다. 
이는 pidx-1번째 테이블 값을 pidx에 갱신해줌으로써 구현할 수 있다.
"""

def build_partial_match_table(K):
    table = [0] * len(K)
    j = 0

    for i in range(1, len(K)):
        # j가 0이 되거나 i, j 같아질 때까지
        while j > 0 and K[i] != K[j]:
            j = table[j - 1]

        # 값이 일치하면 idx 증가하면서 길이 저장
        if K[i] == K[j]:
            j += 1
            table[i] = j

    return table


def solution(S, K):
    s = ''.join([x for x in S if x.isalpha()])

    # KMP 알고리즘을 사용하여 K가 s에 존재하는지 확인
    table = build_partial_match_table(K)
    # print(table)
    j = 0

    for i in range(len(s)):
        # 단어와 패턴이 일치하지 않는 경우 값 변경
        while j > 0 and s[i] != K[j]:
            j = table[j - 1]
            
        # # 만약 pidx가 패턴의 끝까지 도달하였다면, 시작 인덱스 값을 계산하여 추가 후 pidx 값 table의 인덱스에 접근하여 변경
        if s[i] == K[j]:
            if j == len(K) - 1:
                return 1
            j += 1

    return 0

S = input()
K = input()

print(solution(S, K))