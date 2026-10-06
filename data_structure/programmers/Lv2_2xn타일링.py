def solution(n):
    num = 1000000007

    if n == 1:
        return 1
    if n == 2:
        return 2

    """
    visited = [0] * 60002
    visited[1] = 1
    visited[2] = 2

    for i in range(3, n+1):
        visited[i] = visited[i-2] % num + visited[i-1] % num

    return visited[n] % num
    """

    a, b = 1, 1

    for i in range(1, n):
        a, b = b, (a+b) % num

    return b
