def solution(m, n, puddles):
    answer = 0
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    MOD = 1000000007
    m -= 1
    n -= 1

    for rc in range(1, m+n+1):
        for r in range(rc+1):
            c = rc - r
            if ([c+1, r+1] in puddles) or (r > n or c > m):
            # puddles에 포함된 값은 실제 index 값보다 1만큼 크기 때문에 [c+1, r+1]로 값 조정
                continue # puddle을 만났거나, 배열의 범위 밖의 값을 탐색할 때는 continue

            if r > 0:
                dp[r][c] += dp[r-1][c]
            if c > 0:
                dp[r][c] += dp[r][c-1]
            dp[r][c] %= MOD

    answer = dp[-1][-1]

    return answer