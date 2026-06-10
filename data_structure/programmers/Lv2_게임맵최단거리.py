from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])

    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque([[0, 0]])

    while (q): # 진행 가능한 루트가 있다면
        sx, sy = q.popleft()
        for i in range(4):
            nx, ny = sx+dx[i], sy+dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[sx][sy] + 1
                q.append([nx, ny])

    return visited[n-1][m-1] if visited[n-1][m-1] != 0 else -1
