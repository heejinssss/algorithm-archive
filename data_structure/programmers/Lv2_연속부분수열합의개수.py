def solution(elements):
    l = len(elements)
    sum_result = set()

    for i in range(l):
        _sum = elements[i]
        sum_result.add(_sum)
        for j in range(i+1, l+i):
            _sum += elements[j%l]
            sum_result.add(_sum)

    return len(sum_result)
