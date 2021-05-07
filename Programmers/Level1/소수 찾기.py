def primes(n):
    a = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if a[i]:
            for j in range(i+i, n + 1, i):
                a[j] = False
    return [i for i in range(2, n + 1) if a[i]]

def solution(n):
    return len(primes(n))
