# 다시 풀기

def solution(sequence, k):
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
