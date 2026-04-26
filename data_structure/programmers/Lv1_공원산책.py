def solution(park, routes):
    answer = []

    dir = { "E": [0, 1], "W": [0, -1], "S": [1, 0], "N": [-1, 0] }
    lx, ly = len(park), len(park[0])
    sx, sy, flag = 0, 0, False

    for x in range(lx):
        if flag:
            break
        for y in range(ly):
            if park[x][y] == "S":
                sx, sy, flag = x, y, True
                break

    for route in routes:
        d, n = route[0], int(route[2])
        tx, ty, dx, dy = sx, sy, dir[d][0], dir[d][1]
        flag = True

        # for-else
        for i in range(n):
            if lx > tx+dx and tx+dx >= 0 and ly > ty+dy and ty+dy >= 0 and park[tx+dx][ty+dy] != "X":
                tx, ty = tx+dx, ty+dy
            else:
                break
        else:
            sx, sy = tx, ty

    return [sx, sy]
