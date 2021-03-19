def solution(l, r):
    if l==0:
        return 1

    elif l < r:
        return solution(l-1, r) + solution(l, r-1)

    elif l == r:
        return solution(l-1, r)

n = int(input())
result = solution(n, n)
print(result)
