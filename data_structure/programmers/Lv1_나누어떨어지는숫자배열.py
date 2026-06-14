def solution(arr, divisor):
    answer = []
    
    for a in arr:
        if not a % divisor:
            answer.append(a)

    answer.sort()

    return answer if answer else [-1]
