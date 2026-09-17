def solution(n):

    visited = [0, 1, 2, 3] + [0] * (n-3)

    for i in range(4, n+1):
        visited[i] = (visited[i-1] + visited[i-2]) % 1234567

    return visited[n]