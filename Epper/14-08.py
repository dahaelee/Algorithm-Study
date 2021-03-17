from collections import deque

def solution(arr, n, m):
    queue = deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                queue.append((i, j))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if arr[nx][ny] == -1:
                continue

            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))

    for i in range(n):
        if 0 in arr[i]:
            return -1

    return max(map(max, arr)) - 1

m, n = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
result = solution(arr, n, m)
print(result)