# 팩토리얼 예제

def iter(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print(iter(5))
print(fact(5))
