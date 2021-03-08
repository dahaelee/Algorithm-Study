# 나누는 연산을 최대한 많이 해야 횟수가 작다는 정당성

n, k = map(int, input().split())

cnt = 0

while n > 1:
    if n%k == 0:
        n = n//k
        cnt += 1
    else:
        n = n - 1
        cnt += 1

print(cnt)