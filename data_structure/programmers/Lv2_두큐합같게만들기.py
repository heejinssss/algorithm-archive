# 다시 풀기

def solution(queue1, queue2):

    total = sum(queue1) + sum(queue2)

    if total % 2 != 0:
        return -1

    target = total // 2
    count, idx1, idx2 = 0, 0, 0
    _sum = sum(queue1)
    _max = len(queue1) + len(queue2) + 1

    while count <= _max:
        if _sum == target:
            return count
        elif _sum < target:
            _sum += queue2[idx2 % len(queue2)]
            idx2 += 1
        else:
            _sum -= queue1[idx1 % len(queue1)]
            idx1 += 1
        count += 1

    return -1
