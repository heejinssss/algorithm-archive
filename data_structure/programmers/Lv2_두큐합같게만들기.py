# 다시 풀기

def solution(queue1, queue2):

    total = sum(queue1) + sum(queue2)

    if total % 2 != 0:
        return -1

    target = total // 2
    count, idx1, idx2 = 0, 0, 0
    _sum = sum(queue1)
    _max = (len(queue1) * 2) + 1

    while count < _max:
        if _sum < target:
            _sum += queue2[idx2 % len(queue2)]
            idx2 += 1
        elif _sum > target:
            _sum -= queue1[idx1 % len(queue1)]
            idx1 += 1
        else:
            return count
        count += 1

    return count if _sum == target else -1
