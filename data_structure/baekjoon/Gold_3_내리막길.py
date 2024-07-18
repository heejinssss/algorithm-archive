N, M = map(int, input().split())
road = [[0]*(M+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(M+2)]

dp = [[-1]*(M+2) for _ in range(N+2)]
dp[1][1] = 1

def dfs(ci, cj):
    if dp[ci][cj] == -1: # 아직 계산하지 않은 경로에 도달할 경우
        dp[ci][cj] = 0
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            pi, pj = ci+di, cj+dj
            if road[pi][pj] > road[ci][cj]: # 현재 경로가 내리막길이라면
                dp[ci][cj] += dfs(pi, pj)
    
    return dp[ci][cj]         

print(dfs(N, M))