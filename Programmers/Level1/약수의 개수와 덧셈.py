# 약수의 개수를 세어서 반환하는 함수
def fcount(x):
    factors = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            factors.append(i)
            factors.append(x // i)
    return len(set(factors))


def solution(left, right):
    answer = 0
    for x in range(left, right + 1):
        answer += x if fcount(x) % 2 == 0 else - x

    return answer
