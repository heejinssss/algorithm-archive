def solution(sides):

    answer, n = 0, 1

    while n < sum(sides):
        if (max(sides) >= n and max(sides) < min(sides) + n) or (max(sides) < n and n < sum(sides)):
            answer += 1
        n += 1

    return answer
