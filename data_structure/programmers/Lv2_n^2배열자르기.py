"""Time out"""

def solution(n, left, right):

    arr = [[0] * n for _ in range(n)]

    for i in range(n):
        num = i
        while (num >= 0):
            arr[i][num], arr[num][i] = i+1, i+1
            num -= 1

    result = sum(arr, [])

    return result[left:right+1]
