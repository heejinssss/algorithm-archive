def solution(board):
    answer = 0
    n = len(board[0])
    visited = [[0] * n for _ in range(n)]

    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    count = 0

    for i in range(n):
        for j in range(n):
            for k in range(8):
                # 현재 위치가 지뢰이면
                if (board[i][j] == 1):
		                # 탐색되지 않은 지뢰 위치인지 확인
                    if (visited[i][j] == 0):
                        # 지뢰 위치 표시 및 카운트
                        visited[i][j] = 9
                        count += 1
                    # 범위에 포함되는지 확인
                    if (i+di[k] >= 0 and i+di[k] < n and j+dj[k] >= 0 and j+dj[k] < n and visited[i+di[k]][j+dj[k]] == 0):
                        # 지뢰 주변부 표시 및 카운트
                        visited[i+di[k]][j+dj[k]] = 9
                        count += 1

    return n * n - count
