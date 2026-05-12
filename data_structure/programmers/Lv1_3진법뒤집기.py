def solution(n):
    answer = 0
    rlt = ""
    
    while n > 0:
        n, mod = divmod(n, 3)
        rlt += str(mod)

    """
    for i in range(len(rlt)):
        answer += int(rlt[len(rlt)-1-i])*(3**i)
    """
    
    answer = int(rlt, 3)

    return answer
