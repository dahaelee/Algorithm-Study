from collections import deque
import copy


def check(q):
    stack = []

    while q:
        pop = q.popleft()

        # 여는 괄호면
        if pop in ['(', '{', '[']:
            stack.append(pop)

        # 닫는 괄호면
        else:
            if stack and (pop, stack[-1]) in [(')', '('), ('}', '{'), (']', '[')]:
                stack.pop()
            else:
                return 0

    return 1 if not stack else 0


def solution(s):
    q = deque(list(s))
    cnt = 0

    for _ in range(len(q)):
        temp_q = copy.deepcopy(q)
        cnt += check(temp_q)
        q.rotate(-1)

    return cnt
