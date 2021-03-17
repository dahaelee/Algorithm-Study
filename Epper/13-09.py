def solution(n, a):
    d = [0] * 30000
    m = [0] * 30000
    for i in range(len(a)):
        m[i] = a[i]

    d[0] = m[0]
    d[1] = m[0] + m[1]
    d[2] = max(d[1], max(d[0] + m[2], m[1] + m[2]))

    # max(안줍, 줍). 줍 = max(앞에거 안줍, 앞에거 줍)
    for i in range(3, n):
        d[i] = max(d[i - 1], max(d[i - 2] + m[i], d[i - 3] + m[i - 1] + m[i]))

    return d[n - 1]

n = int(input())
a = list(map(int, input().split()))
result = solution(n, a)
print(result)
