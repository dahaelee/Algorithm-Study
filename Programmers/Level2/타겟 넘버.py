from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque([(numbers[0], 0), (-numbers[0], 0)])

    while queue:
        s, i = queue.popleft()
        i += 1

        if i < len(numbers):
            queue.append((s + numbers[i], i))
            queue.append((s - numbers[i], i))

        else:
            if s == target:
                answer += 1

    return answer
