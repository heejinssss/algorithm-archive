# [Best Solution]
N = int(input())

dp = [[0] * 10 for _ in range(N+1)]
dp[1] = [1] * 10 # N이 1일 때

for i in range(2, N+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])

print((sum(dp[-1]))%10007)

# [My Solution]
"""
N = int(input())

before = [1] * 10
dp = [0] * 10

if N == 1:
    print(10)
else:
    for _ in range(N-1):
        for i in range(10):
            dp[i] = sum(before[:i+1])
        before = dp
        dp = [0] * 10
    print((sum(before))%10007)
"""

# [Runtime Error] maximum recursion depth exceeded
"""
def sol(dpList, N):
    global answer

    if N < 0:
        answer = dpList
        return

    dp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(10):
        if i == 0:
            dp[i] = 1
            continue
        dp[i] = sum(dpList[:i+1])
    
    sol(dp, N-1)

dpList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

if N == 1:
    print(10)
else:
    sol(dpList, N-2)
    print(sum(answer)%10007)
"""