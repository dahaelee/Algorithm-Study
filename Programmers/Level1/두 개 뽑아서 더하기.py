import itertools

def solution(numbers):
    answer = []
    for x in itertools.combinations(numbers, 2):
        answer.append(sum(x))
    return sorted(list(set(answer)))
