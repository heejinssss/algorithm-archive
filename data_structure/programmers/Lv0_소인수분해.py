def solution(n):
    answer = []

    num = 2

    while n > 1:
        if n % num == 0:
            if num not in answer:
                answer.append(num)
            n //= num
        else:
            num += 1

    return answer