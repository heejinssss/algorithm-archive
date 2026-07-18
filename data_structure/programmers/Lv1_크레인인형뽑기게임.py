from collections import deque

def solution(board, moves):
    answer = 0
    arr = [ deque() for _ in range(len(board)) ]
    q = deque()

    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i]:
                arr[i].append(board[j][i])

    for move in moves:
        if len(arr[move-1]) > 0:
            a = arr[move-1].popleft()
            q.append(a)
            if len(q) > 1 and q[-1] == q[-2]:
                q.pop()
                q.pop()
                answer += 2

    return answer
