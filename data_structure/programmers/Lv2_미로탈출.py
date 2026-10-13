# 다시 풀기

from collections import deque

def solution(maps):
    n, m, sx, sy = len(maps), len(maps[0]), 0, 0
    visited_L = [[0] * m for _ in range(n)]

    def get_start():
        for i in range(n):
            for j in range(m):
                if maps[i][j] == "S":
                    return i, j

    sx, sy = get_start()

    lx, ly, visited_L = bfs(maps, sx, sy, n, m, visited_L, "L")

    # L까지 도달하지 못한 경우
    if lx == -1:
        return lx

    ex, ey, visited_L = bfs(maps, lx, ly, n, m, visited_L, "E")

    # E까지 도달하지 못한 경우
    if ex == -1:
        return ex

    return visited_L[ex][ey]

# 레버 또는 출구 찾기
def bfs(maps, sx, sy, n, m, visited_L, target):
    q = deque()
    q.append([sx, sy])

    dirx = [0, -1, 0, 1]
    diry = [1, 0, -1, 0]

    if target == "E": # 출구 찾기인 경우에만 visited_E 생성
        visited_E = [[0] * m for _ in range(n)]
        visited_E[sx][sy] = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx+dirx[i], cy+diry[i]

            if target == "E":
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != "X" and visited_E[nx][ny] == 0:
                    visited_L[nx][ny] = visited_L[cx][cy] + 1
                    visited_E[nx][ny] = 1
                    if maps[nx][ny] == "E":
                        return nx, ny, visited_L
                    q.append([nx, ny])
            else:
                if [sx, sy] != [nx, ny] and 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != "X" and visited_L[nx][ny] == 0:
                    visited_L[nx][ny] = visited_L[cx][cy] + 1
                    if maps[nx][ny] == "L":
                        return nx, ny, visited_L
                    q.append([nx, ny])

    return -1, -1, visited_L
