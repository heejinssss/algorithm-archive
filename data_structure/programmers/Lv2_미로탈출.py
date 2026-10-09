from collections import deque

def solution(maps):
    answer = 0

    n, m = len(maps), len(maps[0])
    sx, sy = 0, 0

    FOUND = False

    for i in range(n):
        if FOUND:
            break
        for j in range(m):
            if maps[i][j] == "S":
                sx, sy, FOUND = i, j, True
                break

    lx, ly, visited_L = getL(maps, sx, sy, n, m)

    print(lx, ly, visited_L)

    # L까지 도달하지 못한 경우
    if lx == -1:
        return lx

    # L까지 도달한 경우
    ex, ey, visited_L = getE(maps, lx, ly, n, m, visited_L)

    print(ex, ey, visited_L)

    return visited_L[ex][ey]

# 레버 찾기
def getL(maps, sx, sy, n, m):
    q = deque()
    q.append([sx, sy])

    dirx = [0, -1, 0, 1]
    diry = [1, 0, -1, 0]

    visited_L = [[0] * m for _ in range(n)]

    while q:
        cx, cy = q.pop()
        for i in range(4):
            nx, ny = cx+dirx[i], cy+diry[i]
            if [sx, sy] != [nx, ny] and 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != "X" and visited_L[nx][ny] == 0:
                visited_L[nx][ny] = visited_L[cx][cy] + 1
                if maps[nx][ny] == "L":
                    return nx, ny, visited_L
                q.append([nx, ny])

    return -1, -1, visited_L

# 출구 찾기
def getE(maps, lx, ly, n, m, visited_L):
    q = deque()
    q.append([lx, ly])

    dirx = [0, -1, 0, 1]
    diry = [1, 0, -1, 0]

    visited_E = [[0] * m for _ in range(n)]
    visited_E[lx][ly] = 1

    while q:
        cx, cy = q.pop()
        for i in range(4):
            nx, ny = cx+dirx[i], cy+diry[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != "X" and visited_E[nx][ny] == 0:
                visited_L[nx][ny] = visited_L[cx][cy] + 1
                visited_E[nx][ny] = 1
                if maps[nx][ny] == "E":
                    return nx, ny, visited_L
                q.append([nx, ny])

    return -1, -1, visited_L