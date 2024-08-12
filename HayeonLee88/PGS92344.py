def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    hap = [[0] * (m + 1) for _ in range(n + 1)]
    
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree *= -1

        hap[r1][c1] += degree
        hap[r1][c2 + 1] -= degree
        hap[r2 + 1][c1] -= degree
        hap[r2 + 1][c2 + 1] += degree

    for i in range(n + 1):
        for j in range(1, m + 1):
            hap[i][j] += hap[i][j - 1]
    
    for i in range(1, n + 1):
        for j in range(m + 1):
            hap[i][j] += hap[i - 1][j]
        
    for i in range(n):
        for j in range(m):
            if board[i][j] + hap[i][j] > 0:
                answer += 1
                
    return answer