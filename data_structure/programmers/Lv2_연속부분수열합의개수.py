import itertools

def solution(elements):
    sum_result = set()
    elements = elements + elements[:len(elements)-1]

    # 확인용
    print(elements)

    for i in range(1, len(elements)+1):
        nCi = itertools.combinations(elements, i)
        for lst in list(nCi):
            sum_result.add(sum(lst))

    # 확인용
    print(sum_result)

    return len(sum_result)