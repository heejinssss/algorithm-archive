from itertools import combinations
import math

def solution(nums):
    answer = 0

    for i in combinations(nums, 3):
        if isPrime(sum(i)):
            answer += 1

    return answer

def isPrime(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            num += 1
            return False
    else:
        return True
