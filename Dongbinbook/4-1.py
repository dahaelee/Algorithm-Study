n = int(input())
data = list((input().split()))

x, y = 1, 1

for char in data:
    if char == 'L':
        if y >= 2:
            y -= 1
    elif char == 'R':
        if y <= n-1:
            y += 1
    elif char == 'U':
        if x >= 2:
            x -= 1
    elif char == 'D':
        if x <= n-1:
            x += 1

'''
# 이동방향 
moves = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for char in data:
    for i in range(len(moves)):
        if char == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny
'''

print(x, y)
