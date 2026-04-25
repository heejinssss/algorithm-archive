def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    count = 0
    empty = lottos.count(0)

    for x in lottos:
        if x not in win_nums:
            count += 1

    return [rank[6-(count-empty)], rank[6-count]]
