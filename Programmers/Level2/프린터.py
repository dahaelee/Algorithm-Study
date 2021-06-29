from collections import deque


def solution(priorities, location):
    q = deque([x for x in enumerate(priorities)])
    answer = 1

    while q:
        pmax = max([x[1] for x in q])
        now = q.popleft()

        if now[1] >= pmax:
            if now[0] == location:
                return answer
            answer += 1
        else:
            q.append(now)
