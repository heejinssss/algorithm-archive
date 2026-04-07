def solution(s):
    answer = 0

    answer = (-1) * int(s[1:]) if s[0] == "-" else int(s)
        
    return answer
