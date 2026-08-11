def solution(score):

    """
    answer = []

    rank_score = sorted(score, key=lambda x: (sum(x)), reverse=True)

    cmp = dict()

    for s in score:
        # 동점자가 없으면
        if sum(s) not in cmp.keys():
            cmp[sum(s)] = rank_score.index(s) + 1 # 점수 추가
        answer.append(cmp[sum(s)])

    return answer
    """

    arr = sorted([sum(x) for x in score], reverse=True)

    return [arr.index(sum(x)) + 1 for x in score]
