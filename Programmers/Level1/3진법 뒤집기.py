def solution(n):
    a = []
    while n > 0:
        a.append(n % 3)
        n = n // 3

    answer = 0
    for i, x in enumerate(a[::-1]):
        answer += (3 ** i * x)

    return answer
