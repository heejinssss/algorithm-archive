from collections import deque

def solution(a, b):

    stack = []
    lst = deque(list(str(a/b)))

    for i in range(str(a/b).index(".")+1):
        lst.popleft()

    for i in range(len(lst)):
        stack.append(lst.popleft())
        if stack == list(lst)[:len(stack)]:
            return 2
            break
    else:
        return 1
