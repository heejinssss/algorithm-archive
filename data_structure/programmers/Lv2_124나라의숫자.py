# 다시 풀기

def solution(n):
    answer = ''

    while n > 0:
        remainder = n % 3

        if remainder == 0:
            answer += '4'
            n = n // 3 - 1

        elif remainder == 1:
            answer += '1'
            n = n // 3

        else:
            answer += '2'
            n = n // 3

    return answer[::-1]