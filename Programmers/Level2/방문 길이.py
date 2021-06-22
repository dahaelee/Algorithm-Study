def solution(dirs):
    d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

    x, y = 0, 0
    arr = []

    for i in dirs:

        nx = x + d[i][0]
        ny = y + d[i][1]

        # 공간을 벗어나면 무시
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue

        arr.append((x, y, nx, ny))
        arr.append((nx, ny, x, y))
        x, y = nx, ny

    arr = list(set(arr))

    return len(arr) // 2
