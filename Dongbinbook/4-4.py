n, m = map(int, input().split())
x, y, d = map(int, input().split())

# 리스트에 맵을 이중 리스트로 저장
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 지금까지 방문한 칸을 저장하기 위한 맵
data2 = [[0] * m for _ in range(n)]
data2[x][y] = 1

# d값에 따라 현재 칸 기준 앞으로 한칸 이동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

turn = 0

while True:
    turn_left()

    # 회전한 이후 정면으로 갈 수 있으면 이동
    nx = x + dx[d]
    ny = y + dy[d]
    if data[nx][ny] == 0 and data2[nx][ny] == 0:
        x, y = nx, ny
        data2[x][y] = 1
        turn = 0
    else:
        turn += 1

    # 4방향 다 회전했는데 갈 곳 없는 경우 뒤가 육지면 뒤로, 아니면 종료
    if turn == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if data[nx][ny] == 0:
            x, y = nx, ny
            turn = 0
        else:
            break

# 지금까지 방문한 칸 개수 세기
cnt = 0
for i in range(n):
    cnt += data2[i].count(1)

print(cnt)
