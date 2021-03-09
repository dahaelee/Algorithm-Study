loc = input()

x = int(loc[1])
y = int(ord(loc[0]) - ord('a') + 1)

cnt = 0

# 한 자리에서 이동 가능한 경우의 수 8가지
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

for i in range(8):
    if 1 <= (x + dx[i]) <= 8 and 1 <= (y + dy[i]) <= 8:
        cnt += 1

print(cnt)
