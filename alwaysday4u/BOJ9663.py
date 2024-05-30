import sys
input = sys.stdin.read

def valid(row: int, board: list[int]) -> bool:
    """해당 row에 퀸을 놓을 수 있는지 확인합니다.
    
    Args:
        row (int): 현재 검사하고 있는 행 번호
        board (list[int]): 퀸의 위치를 저장한 리스트

    Returns:
        bool: 현재 행에 퀸을 놓을 수 있다면 True, 그렇지 않다면 False
    """
    for i in range(row):
        if board[row] == board[i] or abs(board[row] - board[i]) == row - i:
            return False
    return True

def dfs(row: int, n: int, board: list[int], visited: list[bool], cnt: list[int]) -> None:
    """깊이 우선 탐색을 사용하여 모든 유효한 퀸의 배치를 찾습니다.
    
    Args:
        row (int): 현재 접근하고 있는 행
        n (int): 체스판의 크기
        board (list[int]): 퀸의 위치를 저장하는 리스트
        visited (list[bool]): 해당 열에 퀸이 있는지 여부를 저장하는 리스트
        cnt (list[int]): 유효한 해결책의 수를 저장하는 리스트
    """
    if row == n:
        cnt[0] += 1
        return
    for i in range(n):
        if not visited[i]:
            board[row] = i
            if valid(row, board):
                visited[i] = True
                dfs(row + 1, n, board, visited, cnt)
                visited[i] = False

n = int(input().strip())
board = [0] * n
visited = [False] * n
cnt = [0]  # 리스트를 사용하여 참조에 의한 전달을 이용
dfs(0, n, board, visited, cnt)
print(cnt[0])
