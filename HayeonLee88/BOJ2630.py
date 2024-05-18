import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
color_dict = {0:0, 1:0}

def search(n, x, y):
	global graph
	color = graph[x][y] # 종이의 색

	for i in range(x, x + n):
		for j in range(y, y + n):
			if graph[i][j] != color: # 한 가지 색으로 이뤄지지 않았을 때
				n //= 2
				search(n, x, y)
				search(n, x, y + n)
				search(n, x + n, y)
				search(n, x + n, y + n)
				return 
	color_dict[color] += 1 # 탐색한 부분이 한 가지 색으로 이뤄졌을 때

search(n, 0, 0)
print(*color_dict.values(), sep='\n')
