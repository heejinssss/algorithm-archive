from collections import deque

def solution(A, B):

    if A == B:
        return 0

    o = deque(B)
    r = deque(A)
    cnt = 0

    while cnt < len(o):

        r = deque([r.pop()]) + r
        cnt += 1

        if o == r:
            return cnt

    return -1
