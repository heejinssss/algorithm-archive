from collections import deque

def solution(s):

    q = deque([s[0]])

    for i in range(1, len(s)):
        if len(q) and q[-1] == s[i]:
            q.pop()
        else:
            q.append(s[i])

    return 1 if not q else 0
