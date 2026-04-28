def solution(wallpaper):
    sx, sy, ex, ey = 50, 50, -1, -1

    for i in range(len(wallpaper)):
        if "#" in wallpaper[i]:
            sx, sy = min(i, sx), min(wallpaper[i].index("#"), sy)
            ex, ey = max(i, ex), max(wallpaper[i].rindex("#"), ey)

    return [sx, sy, ex+1, ey+1]
