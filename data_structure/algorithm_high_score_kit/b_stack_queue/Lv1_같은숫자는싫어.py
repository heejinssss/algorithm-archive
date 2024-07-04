def solution(arr):
    answer = []
    answer.append(arr.pop(0))

    # O(1)
    for num in arr:
        if answer[-1] != num:
            answer.append(num)

    # 시간 초과 (O(N))
    # while arr != []:
    #     if answer[-1] != arr[0]:
    #         answer.append(arr.pop(0))
    #     else:
    #         arr.pop(0)

    return answer