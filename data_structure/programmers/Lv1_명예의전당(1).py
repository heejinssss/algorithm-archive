from collections import deque

# 명예의 전당에 오른 최하위 점수

def solution(k, score):
    answer = []
    dq = deque()

    for s in score:
        dq.append(s)
        dq = sorted(list(dq), reverse=True)
        if len(dq) > k:
            dq.pop()
        answer.append(dq[-1])

    return answer