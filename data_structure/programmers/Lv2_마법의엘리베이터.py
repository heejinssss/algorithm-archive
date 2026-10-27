# 다시 풀기

def solution(storey):
    answer = 0
    c = 10

    while storey > 1:
        if 0 <= storey%c <= 4:  # 0~4
            answer += storey%c
        else:                   # 5~9
            answer += 10-storey%c
            storey += 10
        storey //= c

    return answer
