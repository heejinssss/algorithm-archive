from collections import Counter

def solution(weights):
    count = Counter(weights)
    answer = 0

    # 1:1
    for w, c in count.items():
        answer += c * (c-1) // 2

    for w in count:
        # 2:3
        if (w * 3) % 2 == 0:
            p = (w * 3) // 2
            if p in count:
                answer += count[w] * count[p]

        # 1:2, 2:4
        p = w * 2
        if p in count:
            answer += count[w] * count[p]

        # 3:4
        if (w * 4) % 3 == 0:
            p = (w * 4) // 3
            if p in count:
                answer += count[w] * count[p]

    return answer
