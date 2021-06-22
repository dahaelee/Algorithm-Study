from collections import deque


def solution(prices):
    answer = []
    q = deque(prices)

    while q:
        x = q.popleft()
        t = 0

        for i in q:
            t += 1
            if i < x:
                break

        answer.append(t)

    return answer
