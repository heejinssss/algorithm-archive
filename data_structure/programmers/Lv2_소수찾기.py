import itertools
import math

def solution(numbers):
    answer = 0
    prime = set()

    for i in range(1, len(numbers)+1):
        for p in itertools.permutations(list(numbers), i):
            num = int("".join(p))
            prime.add(num)

    for p in prime:
        if p < 2:
            continue
        for i in range (2, int(math.sqrt(p)+1)): # 2부터 x의 제곱근까지의 숫자
            if p % i == 0:
                break
        else:
            answer += 1

    return answer
