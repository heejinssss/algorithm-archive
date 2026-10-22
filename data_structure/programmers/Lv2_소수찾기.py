# 다시 풀기

import itertools

def solution(numbers):
    answer = 0
    prime = []

    for i in range(1, len(numbers)+1):
        prime.append(list(itertools.permutations(list(numbers), i)))

    print(prime)

    return answer
