import math

def solution(n):
    sqrt = math.sqrt(n)
    # sqrt = n ** (1/2)

    if sqrt % 1 == 0:  # 제곱근이 양의 정수라면
        return (sqrt + 1) ** 2
    else:
        return -1
