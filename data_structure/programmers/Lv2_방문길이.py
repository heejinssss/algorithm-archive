def solution(dirs):
    visited = []
    dic = { "U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0] }
    sx, sy = 0, 0

    for d in dirs:
        nx, ny = sx+dic[d][0], sy+dic[d][1]

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if [sx, sy, nx, ny] not in visited and [nx, ny, sx, sy] not in visited:
                visited.append([sx, sy, nx, ny])
            sx, sy = nx, ny

    return len(visited)
