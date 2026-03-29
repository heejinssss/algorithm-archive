def solution(s):
    answer = ''
    
    for si in s:
        if (s.count(si) == 1):
            answer += si

    return "".join(sorted(answer))
