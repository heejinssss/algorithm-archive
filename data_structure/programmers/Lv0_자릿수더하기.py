def solution(n):

    answer = 0

    for l in list(str(n)):
        answer += int(l)

    return answer
