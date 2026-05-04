import math

def solution(n):

    cnt = 0
    num = 2

    while (num <= n):
        for i in range (2, int(math.sqrt(num)+1)): # 2부터 x의 제곱근까지의 숫자
            if num % i == 0:
                num += 1
                break
        else:
            cnt += 1
            num += 1

    return cnt
