def solution(sequence, k):

    """
    # 시간 초과
    result = []
    l = len(sequence)

    for i in range(l):
        _sum = 0
        for j in range(i, l):
            _sum += sequence[j]
            if _sum > k:
                break
            if _sum == k:
                result.append([i, j])

    return sorted(result, key=lambda x:(x[1]-x[0], x[0]))[0]
    """

    start = 0
    total = 0
    answer = [0, len(sequence)-1]

    for end in range(len(sequence)):
        total += sequence[end]

        while total > k:
            # 1. total에서 왼쪽 원소를 빼기
            total -= sequence[start]
            # 2. start 이동
            start += 1

        if total == k:
            # 3. 기존 answer보다 구간 길이가 짧으면 갱신
            if answer[1]-answer[0] > end-start:
                answer = [start, end]

    return answer
