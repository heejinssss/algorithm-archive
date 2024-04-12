n = int(input())
lst = [0] + [int(input()) for _ in range(n)]

# dp 테이블 생성 및 초기화
dp = [[0]*3 for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) # 안 밟음, 즉 직전까지 1~2번 밟음
    dp[i][1] = dp[i-1][0]+lst[i] # 1번 밟음, 즉 직전까지 0번 밟음
    dp[i][2] = dp[i-1][1]+lst[i] # 2번 밟음, 즉 직전까지 1번 밟음

print(max(dp[n][1], dp[n][2]))