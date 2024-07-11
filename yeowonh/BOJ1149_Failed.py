# 시간 개빡빡하네 반복문 주의할 것
# 1번부터 N번 집
# 규칙을 만족하며 모든 집을 칠하는 비용의 최소값
# 1번 집은 2번집과 같지 않음
# N번 집은 N-1번집과 같지 않음
# i번 집은 양옆집과 같지 않음

'''

dp[1] 일 때 26, R
dp[2] 일 때 49, R

dp[1]을 바꿀지 dp[2]를 바꿀지
26+57 VS 40+49 -> 26 57이 더 작음
dp[2]를 57, B로 바꾸기

dp[2] 일 때 57, B

dp[3]일 때 13, R
dp[3]일 때 13, R


-----

dp[1]일 때 1, R
같을 경우 -> 앞뒤와 같지 않은 아무거나
dp[2]일 때 


1. R : 가격, G : 가격, B : 가격 식으로 딕셔너리 형태 만들기
2. 가격 크기 순으로 오름차순 정렬
3. dp list([cost, color]), color list 따로 지정


'''

def solution(N):
    dp = [[None, 0] for _ in range(N)] 
    cost = [{} for _ in range(N)]

    for i in range(N):
        r,g,b = map(int, input().split())
        cost[i]['R'] = r; cost[i]['G'] = g; cost[i]['B'] = b
        # cost 오름차순 정렬
        cost[i] = sorted(cost[i].items(), key=lambda x : x[1])

    # 오름차순 정렬 보장
    # 1번째 집의 /1번째로 작은
    dp[0] = list(cost[0][0])
    # print(dp[0])

    for i in range(1, N):
        # 전집과 색 일치하는지 확인
        if cost[i][0][0] == dp[i-1][0]:
            # 이전 dp[i-1]의 가격과 색을 갱신
            if cost[i-1][1][1] + cost[i][0][1] < dp[i-1][1] + cost[i][1][1]:
                # 전집의 2번째로 작은 가격의 색깔이 전전집의 2번째로 작은 가격의 색깔과 같은지 추가 검증
                # 같을 경우 3번째로 더하기
                if i >= 2 and cost[i-1][1][0] == dp[i-2][0]:
                    dp[i-1] = [cost[i-1][2][0], dp[i-1][1] + (cost[i-1][2][1] - dp[i-1][1])]

                else:
                    # 추가된 가격만큼을 더해주기
                    dp[i-1] = [cost[i-1][1][0], dp[i-1][1] + (cost[i-1][1][1] - dp[i-1][1])]

            # 현재 집을 2번째 가격으로 
            else:
                dp[i] = [cost[i][1][0], dp[i-1][1] + cost[i][1][1]]
            
        # 전집과 색깔 일치하지 않을 경우
        else:
            # 색깔 기록, 가격 더하기
            dp[i] = [cost[i][0][0], dp[i-1][1] + cost[i][0][1]]

    return dp[N-1][1]

N = int(input())
print(solution(N))