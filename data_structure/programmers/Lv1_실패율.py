def solution(N, stages):
    answer = []

    rank = { x: 0 for x in range(1, N+1) }

    # 각 스테이지에 있는 사람 수
    stage_cnt = [0] * (N+2)

    for stage in stages:
        stage_cnt[stage] += 1

    cur = len(stages)

    for i in range(1, N+1):
        count = stage_cnt[i] # i 스테이지에 있는 사람 수

        if cur == 0:
            rank[i] = 0
        else:
            rank[i] = count / cur

        cur -= count

    answer = sorted(rank.keys(), key=lambda x: (-rank[x], x))

    return answer