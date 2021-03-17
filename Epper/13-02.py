def solution(m, n):
    c = m - n
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = 0
    t = 0
    for x in money:
        if (c // x) > 0:
            cnt += (c // x)
            t += 1
        c = c % x

    return t, cnt

m = int(input())
n = int(input())
a, b = solution(m, n)
print(a, b)
