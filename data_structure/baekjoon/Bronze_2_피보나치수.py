# 시간 초과
# N = int(input())

# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n-1) + f(n-2)

# print(f(N))

N = int(input())

dp = [0] * (N+1)
dp[0] = 0
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])