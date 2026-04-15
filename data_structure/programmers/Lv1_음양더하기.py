def solution(absolutes, signs):
    answer = 0
    
    for a, s in zip(absolutes, signs):
        answer += a if s else (-1) * a
        
    return answer
