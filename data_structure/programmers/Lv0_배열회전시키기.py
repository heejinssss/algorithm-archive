def solution(numbers, direction):

    """
    answer = [0] * len(numbers)
    
    if direction == "left":
        for i in range(len(numbers)-1):
            answer[i] = numbers[i+1]
        answer[len(numbers)-1] = numbers[0]
    else:
        for i in range(len(numbers)-1):
            answer[i+1] = numbers[i]
        answer[0] = numbers[len(numbers)-1]
    """
    
    answer = numbers[1:] + numbers[:1] if direction == "left" else numbers[-1:] + numbers[:-1]

    return answer
