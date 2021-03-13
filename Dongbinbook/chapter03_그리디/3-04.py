n, m = map(int, input().split())

result = 0

for i in range(n):
    row = list(map(int, input().split()))
    min_value = 10001 # 최대 수보다 큰 수
    for j in row:
        min_value = min(min_value, j)
    result = max(result, min_value)

print(result)
