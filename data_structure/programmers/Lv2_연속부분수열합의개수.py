def solution(elements):
    sum_result = set()
    elements = elements + elements[:len(elements)-1]

    # 확인용
    print(elements)

    # 연속 부분 수열의 원소 개수
    # ?
    for i in range(len(elements)):
        for j in range(len(elements)-i):
            sum_result.add(sum(elements[j:j+i+1]))

    # 확인용
    print(sum_result)

    return len(sum_result)