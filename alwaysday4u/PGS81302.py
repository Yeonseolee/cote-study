def solution(places):
    answer = []
    for place in places:
        ans = True

        for i in range(5):
            if not ans:
                break
            for j in range(5):
                if not ans:
                    break
                if place[i][j] == "P": 
                    if i+1<5:
                        if place[i+1][j] == "P":
                            ans = False
                            break
                        if place[i+1][j] == "O":
                            if i+2<5:
                                if place[i+2][j] == "P":
                                    ans = False
                                    break
                    if j+1<5:
                        if place[i][j+1] == "P":
                            ans = False
                            break
                        if place[i][j+1] == "O":
                            if j+2<5:
                                if place[i][j+2] == "P":
                                    ans = False
                                    break
                    if i+1<5 and j+1<5:
                        if place[i+1][j+1] == "P" \
                        and (place[i+1][j] == "O" or place[i][j+1] == "O"):
                            ans = False
                            break
                    if i+1<5 and j-1>=0:
                        if place[i+1][j-1] == "P" \
                        and (place[i+1][j] == "O" or place[i][j-1] == "O"):
                            ans = False
                            break

        answer.append(int(ans))

    return answer
