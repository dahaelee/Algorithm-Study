from collections import deque

n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

# 첫 시작 노드 큐에 넣음. 최단거리 1.
queue.append((0, 0))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 미로 밖이면 무시
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 해당 노드가 1이면 방문하고 큐에 넣고 최단거리 갱신
        if data[nx][ny] == 1:
            queue.append((nx, ny))
            data[nx][ny] = data[x][y] + 1

print(data[n - 1][m - 1])
