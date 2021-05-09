def solution(a, b):
    a, b = (b, a) if a > b else (a, b)
    l = [x for x in range(a, b + 1)]
    return sum(l)
