def solution(n, numlist):
    answer = []

    for num in numlist:
        if not num % n:
            answer.append(num)

    return answer
