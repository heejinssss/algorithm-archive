from collections import deque

def solution(order):
    cnt = 0
    idx = 0

    arr = deque(range(1, len(order)+1))
    stack = []

    while True:
        if arr and order[idx] == arr[0]:
            arr.popleft()
            idx += 1
            cnt += 1

        elif stack and order[idx] == stack[-1]:
            stack.pop()
            idx += 1
            cnt += 1

        elif arr:
            stack.append(arr.popleft())

        else:
            break

    return cnt
