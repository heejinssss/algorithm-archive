def solution(board, h, w):
    answer = 0
    n = len(board)

    for x, y in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
        if 0 <= h+x < n and 0 <= w+y < n and board[h][w] == board[h+x][w+y]:
            answer += 1

    return answer
