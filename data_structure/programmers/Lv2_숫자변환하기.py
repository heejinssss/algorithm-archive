def solution(x, y, n):

    visited = [0] * (y+1)
    case = [[y, 0]]
    result = []

    while case:
        cur, cnt = case.pop(0)

        if cur == x:
            result.append(cnt)
            continue

        if cur < 1:
            continue

        if cur%2 == 0 and visited[cur//2] == 0 and cur >= x:
            case.append([cur//2, cnt+1])
            visited[cur//2] = 1

        if cur%3 == 0 and visited[cur//3] == 0 and cur >= x:
            case.append([cur//3, cnt+1])
            visited[cur//3] = 1

        if visited[cur-n] == 0 and cur >= x:
            case.append([cur-n, cnt+1])
            visited[cur-n] = 1

    if not len(result):
        return -1

    return min(result)
