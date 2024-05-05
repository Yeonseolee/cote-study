def solution(numbers, hand):
    answer = ''
    
    loc = {1: ["L", (0, 0)], 4: ["L", (1, 0)], 7: ["L", (2, 0)],
           3: ["R", (0, 2)], 6: ["R", (1, 2)], 9: ["R", (2, 2)],
           2: ["X", (0, 1)], 5: ["X", (1, 1)], 8: ["X", (2, 1)], 0: ["X", (3, 1)], 
           "L": (3, 0), "R": (3, 2)}
    
    for n in numbers:
        pos = loc[n][0]
        x, y = loc[n][1]
        if pos == "X":
            left_sum = abs(x - loc["L"][0]) + abs(y - loc["L"][1])
            right_sum = abs(x - loc["R"][0]) + abs(y - loc["R"][1])
            if left_sum < right_sum:
                answer += "L"
                loc["L"] = (x, y)
            elif left_sum > right_sum:
                answer += "R"
                loc["R"] = (x, y)
            else:
                if hand == "right":
                    answer += "R"
                    loc["R"] = (x, y)
                else:
                    answer += "L"
                    loc["L"] = (x, y)
        else:
            loc[pos] = (x, y)
            answer += pos

    return answer