import math

def solution(number, limit, power):
    answer = 1

    for i in range(2, number+1):
        num, cnt = 1, 0
        sqrt = int(math.sqrt(i))

        while num <= sqrt:
            if not i%num:
                cnt += 1
            num += 1

        result = cnt*2-(1 if i == sqrt*sqrt else 0)

        if result > limit:
            answer += power
        else:
            answer += result

    return answer
