from collections import Counter

def solution(X, Y):	
    arr = []
    sList = X if len(X) < len(Y) else Y # 기준
    cList = X if len(X) >= len(Y) else Y # 비교
    counter = Counter(cList)

    for s in sList:
        if counter[s] > 0:
            arr.append(s)
            counter[s] -= 1

    if not len(arr):
        return "-1"
    elif len(arr) == arr.count("0"):
        return "0"
    else:
        arr = sorted(arr, reverse=True)
        return "".join(arr)
