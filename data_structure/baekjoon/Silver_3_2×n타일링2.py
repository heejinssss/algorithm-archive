# 규칙 찾기
# i번째 직사각형 만드는 방법
# (1) [(i-1)번째 직사각형의 우측에 (2X1) 타일을 추가한다]
# (2) [(i-2)번째 직사각형의 우측에 (2X2) 타일 1개 또는 (2X1) 타일 2개를 추가한다]

N = int(input())
answer = 0
dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2] * 2 # 5는 4+3

answer = dp[-1]

print(answer % 10007)