def solution(nums):
    answer = 0
    N = len(nums)
    n = len(set(nums))
    if N // 2 > n:
        answer = n
    else:
        answer = N // 2
    return answer