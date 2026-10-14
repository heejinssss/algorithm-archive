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

"""
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])

    def bfs(start, target):
        visited = [[-1] * m for _ in range(n)]
        sx, sy = start
        visited[sx][sy] = 0
        q = deque([(sx, sy)])

        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]

        while q:
            x, y = q.popleft()

            if maps[x][y] == target:
                return visited[x][y], (x, y)

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if not (0 <= nx < n and 0 <= ny < m):
                    continue

                if maps[nx][ny] == "X" or visited[nx][ny] != -1:
                    continue

                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

        return -1, None

    # 시작점 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i, j)

    # 시작점 -> 레버
    dist1, lever = bfs(start, "L")
    if dist1 == -1:
        return -1

    # 레버 -> 출구
    dist2, exit_pos = bfs(lever, "E")
    if dist2 == -1:
        return -1

    return dist1 + dist2
"""