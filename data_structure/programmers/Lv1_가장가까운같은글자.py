def solution(s):
    idx = dict()
    answer = []

    for i in range(len(s)):
        if s[i] not in idx:
            answer.append(-1)
        else:
            answer.append(i-max(idx[s[i]]))
        idx[s[i]] = [i]

    return answer
