def solution(x):
    answer = True

    num = 0

    for i in str(x):
        num += int(i) 

    answer = False if x % num else True

    return answer
