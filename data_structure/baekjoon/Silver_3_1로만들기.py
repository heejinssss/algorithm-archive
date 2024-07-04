N = int(input())

dp = [0] * (N+1) # dp[1] = 0으로 초기값 설정

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1 # +1
    if i % 2 == 0: # x가 2의 배수인 경우
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0: # x가 3의 배수인 경우
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])