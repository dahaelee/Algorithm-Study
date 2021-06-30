from itertools import permutations


def prime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True


def solution(numbers):
    pool = list(numbers)  # 쓸 수 있는 숫자 pool
    result = [int(n) for n in pool]  # 만든 숫자 list

    for i in range(2, len(pool) + 1):
        for p in permutations(pool, i):
            result.append(int(''.join(p)))

    result = list(set(result))

    return [prime(x) for x in result if x != 0].count(True)
