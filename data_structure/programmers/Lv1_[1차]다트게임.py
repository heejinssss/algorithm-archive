from collections import deque

def solution(dartResult):

    score = { "S": 1, "D": 2, "T": 3 }
    bonus = { "*": 2, "#": -1 }
    num = deque()
    tmp = ""

    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            tmp += dartResult[i]
        else:
            if dartResult[i] in score.keys():
                cur = int(tmp)
                tmp = ""
                cur **= score[dartResult[i]]
            if dartResult[i] in bonus.keys():
                cur = num.pop()
                cur *= bonus[dartResult[i]]
            if 0 <= i+3 < len(dartResult) and dartResult[i+3] == "*":
                cur *= 2
            num.append(cur)

    return sum(num)
