def solution(arr1, arr2):
    answer = []

    for fst, scd in zip(arr1, arr2):
        arr = []
        for f, s in zip(fst, scd):
            arr.append(f+s)

        answer.append(arr)

    return answer
