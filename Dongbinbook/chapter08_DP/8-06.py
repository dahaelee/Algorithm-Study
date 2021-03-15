n = int(input())
array = list(map(int, input().split()))

# 왼쪽부터 차례대로 털지 안 털지 결정한다고 생각

d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])
