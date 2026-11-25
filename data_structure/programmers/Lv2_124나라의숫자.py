# 다시 풀기

def solution(n):
    answer = ''

    while n > 0:
        mod = n % 3

        if mod == 0:
            answer += '4'
            n = n // 3 - 1

        elif mod == 1:
            answer += '1'
            n = n // 3

        else:
            answer += '2'
            n = n // 3

    return answer[::-1]