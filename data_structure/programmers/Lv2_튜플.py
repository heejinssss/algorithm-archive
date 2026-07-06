def solution(s):
    answer = []

    arr = s[2:len(s)-2].split("},{")
    arr = sorted(arr, key=lambda x : len(x))

    for a in arr:
        aList = a.split(",")
        print(aList)

    return answer
