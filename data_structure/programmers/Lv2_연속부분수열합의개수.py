import itertools

def solution(elements):
    sum_result = set()

    for i in range(1, len(elements)):
        nCi = itertools.combinations(elements, i)
        for lst in list(nCi):
            sum_result.add(sum(lst))

    return len(sum_result)