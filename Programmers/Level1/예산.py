def solution(d, budget):
    d.sort()
    cnt = 0

    for x in d:
        budget -= x
        if budget < 0:
            break
        cnt += 1

    return cnt
