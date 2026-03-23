def solution(num_list, n):

    total = len(num_list)
    arr_len = total // n

    arr = [[0] * n for _ in range(arr_len)]

    for i in range(arr_len):
        for j in range(n):
            arr[i][j] = num_list[i*n+j]

    return arr
