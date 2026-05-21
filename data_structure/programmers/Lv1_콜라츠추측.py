def solution(num):
    cnt = 0

    while (cnt <= 500):

        if num == 1: # 1인 경우 0 출력
            return cnt

        num = num * 3 + 1 if num % 2 else num // 2
        cnt += 1

    return -1
