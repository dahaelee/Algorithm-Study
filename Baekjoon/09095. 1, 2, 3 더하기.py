# a(i) = a(i-1) + a(i-2) + a(i-3)
# a(1) = 1, a(2) = 2, a(3) = 4

t = int(input())

d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 11):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for _ in range(t):
    x = int(input())
    print(d[x])
