import itertools

def prime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(nums):
    cnt = 0

    for c in itertools.combinations(nums, 3):
        if prime(sum(c)):
            cnt += 1

    return cnt
