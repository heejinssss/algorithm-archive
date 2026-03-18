def solution(n):
    answer = 0
    num = 2

    while (num <= n):
        if (not (num % 2)):
            answer += num
        num += 1

    return answer
