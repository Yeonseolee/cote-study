'''
4:39~
감소하는 수: 0과 앙의 정수인 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소할 때
- 감소하는 수 = 321, 950
- 감소하는 수 x = 322, 958

N번째 감소하는 수를 출력하는 프로그램 작성
0: 0번째 감소하는 수
1: 1번째 감소하는 수
만약 N번째 감소하는 수가 없다면 -1 출력
0 <= N <= 1,000,000

0, 1, 2, 3, 4, 5, 6, 7, 8, 9

n _ _: 첫째자리가 n이라면 그 이하의 자릿수는 n 이하의 수
10 20 21 30 31 32 40 41 42 43 ... 
210 310 320 410 420 421 430 431 432
9876543210이 최대 감소하는 수
987654321
987654320
987654310

'''
import sys

sys.setrecursionlimit(10000000)

n = int(input())

array = [-1] * (n + 1)
num = "0"

def check():
    global num
    if num == "9876543210":
        return -1
    pre = num[0]

    for i, x in enumerate(num[1:]):
        if x >= pre:
            num = str(int(num) % 10 * 10 + (10 ** (i + 1)))
            check()
            break
        pre = x
    return num

for i in range(n + 1):
    array[i] = check()
    if array[i] == -1:
        break
    num = str(int(num) + 1)
    
print(array)