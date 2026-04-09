def solution(n):
    """
    answer = []
    
    for x in str(n)[::-1]:
        answer.append(int(x))

    return answer
    """
    return list(map(int, reversed(str(n))))
