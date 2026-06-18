def solution(left, right):
    answer = 0

    """
    for i in range(left, right+1):
        num, cnt = 1, 0
        while (num < i):
            if not i % num:
                cnt += 1
            num += 1
        if not cnt % 2:
            answer -= i
        else:
            answer += i
    """

    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i

    return answer
