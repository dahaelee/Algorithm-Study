from math import ceil
from collections import deque


def solution(progresses, speeds):
    q = deque([ceil((100 - p) / s) for p, s in zip(progresses, speeds)])

    answer = []

    x = q.popleft()
    cnt = 1

    while q:
        now = q.popleft()

        if now <= x:
            cnt += 1
        else:
            answer.append(cnt)
            x = now
            cnt = 1

    answer.append(cnt)

    return answer
