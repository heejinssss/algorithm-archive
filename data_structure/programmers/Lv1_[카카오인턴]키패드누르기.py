def solution(numbers, hand):
    answer = ""

    pad = { 1: [0,0], 2: [0,1], 3: [0,2], 4: [1,0], 5: [1,1], 6: [1,2], 7: [2,0], 8: [2,1], 9: [2,2], 0: [3,1] }

    lx, ly, rx, ry = 3, 0, 3, 2

    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            lx, ly = pad[number]
        elif number in [3, 6, 9]:
            answer += "R"
            rx, ry = pad[number]
        else:
            cx, cy = pad[number]
            if abs(cx-rx)+abs(cy-ry) > abs(cx-lx)+abs(cy-ly): # 왼손이 더 가까운 경우
                answer += "L"
                lx, ly = pad[number]
            elif abs(cx-rx)+abs(cy-ry) < abs(cx-lx)+abs(cy-ly): # 오른손이 더 가까운 경우
                answer += "R"
                rx, ry = pad[number]
            else: # 두 엄지 손가락이 같은 거리에 있는 경우
                if hand == "right":
                    answer += "R"
                    rx, ry = pad[number]
                else:
                    answer += "L"
                    lx, ly = pad[number]

    return answer
