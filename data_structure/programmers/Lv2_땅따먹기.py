def solution(land):
    cand = []

    for i in range(4):
        prev_index = i
        value = land[0][i]
        for j in range(1, len(land)):
            land[j][prev_index] = 0
            value += max(land[j])
            prev_index = land[j].index(max(land[j]))
        cand.append(value)

    return max(cand)
