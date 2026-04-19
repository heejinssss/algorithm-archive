def solution(n):
    answer = n-1
    
    for i in range(n-1, 0, -1):
        if n % i == 1:
            answer = min(answer, i)
        
    return answer
