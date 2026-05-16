def solution(k, m, score):
    answer = 0
    
    num = len(score)//m

    score = sorted(score)
    
    for i in range(0, num*m, m):
        answer += score[i+(len(score)-num*m)]*m

    return answer