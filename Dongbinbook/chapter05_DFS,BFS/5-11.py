from collections import deque

n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input())))

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x, y)) # 시작 노드 삽입

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft() # 튜플의 원소를 변수 여러개에 한번에 할당하는 방법 (언패킹)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 해당 노드가 1일때만 최단 거리 기록 (방문한 적 없고, 벽이 아님)
            if data[nx][ny] == 1:
                data[nx][ny] = data[x][y] + 1
                queue.append((nx, ny))

    # 출구 노드의 방문 순서 반환
    return data[n-1][m-1]

print(bfs(0,0))
print(data)

# 해당 노드가 1일때 방문해 최단 거리 기록을 하다 보니, 예외적으로 첫번째 노드는 방문한 적 있는데도 다시 방문하게 됨.
# 그러나 가장 오른쪽 아래로 이동하는 것을 요구하고 있으므로 정답에는 영향 없음.
