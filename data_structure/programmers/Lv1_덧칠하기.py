def solution(n, m, section):
    answer = 1
    pivot = section[0]

    for i in range(1, len(section)):
        if section[i]-pivot+1 <= m:
            continue
        answer += 1
        pivot = section[i]

    return answer