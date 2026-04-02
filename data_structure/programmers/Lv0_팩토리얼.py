def solution(n):
    answer = 1
    num = 0
    
    while (answer * num < n):
        num += 1
        answer *= num

    return num
