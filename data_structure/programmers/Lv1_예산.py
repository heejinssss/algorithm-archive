def solution(d, budget):
    answer = 0
    
    d = sorted(d)
    
    for i in d:
        if budget-i >= 0:
            budget, answer = budget-i, answer+1
            continue
        break

    return answer