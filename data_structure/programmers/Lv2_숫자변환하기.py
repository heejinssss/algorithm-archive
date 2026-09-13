def solution(x, y, n):
    answer = 0

    case = [[y, 0]]
    result = []

    while case:
        cur, cnt = case.pop(0)
        if cur <= x:
            if cur == x:
                return cnt
            else:
                return -1
        if cur >= x and cur%2 == 0:
            case.append([cur//2, cnt+1])
        if cur >= x and cur%3 == 0:
            case.append([cur//3, cnt+1])
        if cur >= x:
            case.append([cur-n, cnt+1])

    return answer
