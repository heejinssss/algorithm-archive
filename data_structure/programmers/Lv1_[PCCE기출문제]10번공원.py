def solution(mats, park):

    answer = -1
    maxV = 0

    w = len(park[0])
    h = len(park)

    dp = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if i == 0 or j == 0:
                dp[i][j] == 1
            if park[i][j] == "-1":
                dp[i][j] = min([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]]) + 1
                maxV = max(maxV, dp[i][j])

    mats = sorted(mats, reverse=True)

    for mat in mats:
        if mat <= maxV:
            answer = mat
            break
    else:
        return -1

    return answer
