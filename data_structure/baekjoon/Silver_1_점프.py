def myDP(N, board, dp):
    for i in range(N):
        for j in range(N):
            if dp[i][j] > 0 and board[i][j] > 0: # 이동 가능 경로가 존재하고, 1 이상 이동할 수 있다면
                canmove = board[i][j]
                if i+canmove < N:
                    dp[i+canmove][j] += dp[i][j]
                if j+canmove < N:
                    dp[i][j+canmove] += dp[i][j]
    
    return dp[-1][-1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

print(myDP(N, board, dp))

# [Time out]
"""
def myDP(N, board):
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = 1 # dp[i][j]까지 올 수 있는 경로의 개수

    q = []
    q.append([0, 0])

    while q:
        sx, sy = q.pop(0)

        if board[sx][sy] == 0 and sx != N-1 and sy != N-1: # 골인 지점 전에 0으로 점프한 경우
            dp[sx][sy] = 0 # 가능한 경우의 수(코스) 초기화
            continue

        nx = sx + board[sx][sy] # 아래로 이동한 경우
        ny = sy + board[sx][sy] # 옆으로 이동한 경우

        if nx < N:
            dp[nx][sy] += dp[sx][sy]
            if nx == N-1 and sy == N-1:
                continue
            q.append([nx, sy])
    
        if ny < N:
            dp[sx][ny] += dp[sx][sy]
            if sx == N-1 and ny == N-1:
                continue
            q.append([sx, ny])

    return dp[-1][-1]
"""