def solution(n):
    if n % 15 == 0:
        q = n // 15
        r = 15
    else:
        q = (n // 15) + 1
        r = (n % 15)
    return q, r

n = int(input())
q, r = solution(n)
print(q, r)
