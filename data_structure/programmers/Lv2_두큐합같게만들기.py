def solution(queue1, queue2):

    total = sum(queue1) + sum(queue2)

    if total % 2 != 0:
        return -1

    arr = queue1 + queue2
    n = len(queue1)

    target = total // 2
    count, l, r = 0, 0, n
    _sum = sum(queue1)
    _max = (len(queue1) + len(queue2)) * 2

    while count <= _max:
        if _sum == target:
            return count

        if _sum < target:
            _sum += arr[r % len(arr)]
            r += 1
        else:
            _sum -= arr[l % len(arr)]
            l += 1
        count += 1

    return -1
