T = int(input())

for test_case in range(1, T+1):
    n = int(input()) # n by n 미로
    arr = []
    for _ in range(n):
        a = list(input())
        arr.append(a)

    # 출발점 찾기
    sx = sy = 0
    for si in range(n):
        if '2' in arr[si]:
            sx = si
            for sj in range(n):
                if arr[si][sj] == '2':
                    sy = sj

    q = [[sx, sy]]
    visited = [[0]*n for _ in range(n)]
    flag = True

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    while q:
        sx, sy = q.pop(0)
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] != '1' and arr[nx][ny] != '2':
                visited[nx][ny] = visited[sx][sy] + 1
                q.append([nx, ny])
                if arr[nx][ny] == '3':
                    flag = False
                    print(f'#{test_case} {visited[sx][sy]}')
                    break

    if flag:
        print(f'#{test_case} {0}')