def solution(numbers):
    answer = -1

    std = [0,1,2,3,4,5,6,7,8,9]

    answer = sum([x for x in std if x not in numbers])

    return answer
