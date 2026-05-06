def solution(n, arr1, arr2):
    answer = []

    for a1, a2 in zip(arr1, arr2):
        cnt = ""
        # a1, a2 = (n-len(format(a1, "b")))*"0"+format(a1, "b"), (n-len(format(a2, "b")))*"0"+format(a2, "b")
        a1, a2 = format(a1, "b").rjust(n, "0"), format(a2, "b").rjust(n, "0")
        for i in range(n):
            cnt = cnt+"#" if int(a1[i]) or int(a2[i]) else cnt+" "
        answer.append(cnt)

    return answer