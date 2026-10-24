# 다시 풀기

import itertools

def solution(numbers):
    answer = 0
    prime = set()

    for i in range(1, len(numbers)+1):
        for p in itertools.permutations(list(numbers), i):
            num = int("".join(p))
            prime.add(num)

    print(prime)

    for p in prime:
        pass

    return answer
