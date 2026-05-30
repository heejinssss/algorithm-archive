def solution(sizes):
    w, h = 0, 0

    for size in sizes:
        w = max(min(size[0], size[1]), w)
        h = max(max(size[0], size[1]), h)

    return w * h