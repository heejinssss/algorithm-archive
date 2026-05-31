def solution(s):

    sArr = list(map(int, s.split(" ")))
            
    answer = str(min(sArr)) + " " + str(max(sArr))
    
    return answer