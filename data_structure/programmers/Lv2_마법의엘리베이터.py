def solution(storey):
    answer = 0

    while storey >= 1:
        if 0 <= storey%10 <= 4:     # 0~4
            answer += storey%10
        elif storey%10 == 5:        # 5
            answer += 5
            if 55 <= storey%100 <= 95:
                storey += 10
        else:                       # 6~9
            answer += 10-(storey%10)
            storey += 10
        storey //= 10

    return answer
