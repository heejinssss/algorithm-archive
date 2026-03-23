def solution(numbers, k):

    n = len(numbers)
    t = (k - 1) * 2 # 타겟 인덱스
    
    return numbers[t % n]