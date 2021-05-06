def solution(n):
    # n까지의 모든 수를 확인할 필요 없이 n/2까지만 확인하면 된다.
    l = [i for i in range(1, n // 2 + 1) if n % i == 0]

    answer = sum(l) + n
    return answer
