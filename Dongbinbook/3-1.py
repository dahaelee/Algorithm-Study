n = 1260
cnt = 0

coins = [500, 100, 50, 10]

for i in coins:
    cnt += n // i
    n %= i

print(cnt)