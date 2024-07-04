# N의 경우의 수가 50보다 작기 때문에 백트래킹 활용 가능
# 그 이상의 범위일 경우, dp 또는 greedy 고려

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

# n: 종료 조건(날짜)
# sm: 현재까지의 상담 수입
# ans: 이전 루틴의 상담 수입

def dfs(n, sm):
    global ans
    # [1] 종료 조건: 가능하면, n을 종료에 관련된 것으로 설정
    if n >= N:
        ans = max(ans, sm)
        return
    # 하부 호출
    # (1) 다음 상담을 진행하고 싶다면
    if (n + T[n] <= N):
        dfs(n + T[n], sm + P[n])
    # (2) 다음 상담을 진행하지 않는다면
    dfs(n + 1, sm)

ans = 0
dfs(0, 0)
print(ans)