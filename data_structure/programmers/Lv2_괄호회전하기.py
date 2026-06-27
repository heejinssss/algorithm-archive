from collections import deque

def solution(s):
    answer = 0

    for _ in range(len(s)):
        q = deque()
        ok = True

        for ch in s:
            if ch in "([{":
                q.append(ch)
            else:
                if not q:
                    ok = False
                    break

                if ch == ")" and q[-1] == "(":
                    q.pop()
                elif ch == "]" and q[-1] == "[":
                    q.pop()
                elif ch == "}" and q[-1] == "{":
                    q.pop()
                else:
                    ok = False
                    break

        if ok and not q:
            answer += 1

        s = s[1:] + s[0]

    return answer