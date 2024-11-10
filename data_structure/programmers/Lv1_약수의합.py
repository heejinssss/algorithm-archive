def solution(n):    
    result = []
    l = 1

    while l <= n:
        if (n % l) == 0:
            result.append(l)
        l += 1
        
    return sum(result)