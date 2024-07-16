N, M = map(int, input().split())
dp = [[0]*(M+1)] + [[0]+list(map(int, input().split())) for _ in range(N)]

for x in range(1, N+1):
    for y in range(1, M+1):
        dp[x][y] += max(dp[x-1][y], dp[x][y-1])

print(dp[-1][-1])