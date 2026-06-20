def solution(food):
    answer = ""
    
    for x in range(1, len(food)):
        answer += str(x)*(food[x]//2)

    return answer+"0"+answer[::-1]
