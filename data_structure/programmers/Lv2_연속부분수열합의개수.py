def solution(elements):
    l = len(elements)
    sum_result = set()
    elements = elements + elements[:len(elements)-1]

    for i in range(l):
        for j in range(l):
            sum_result.add(sum(elements[j:j+i+1]))

    return len(sum_result)