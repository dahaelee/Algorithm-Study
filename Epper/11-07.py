def solution(n, scores):
    scores.sort()

    m = scores[0]

    for x in scores:
        m = (m + x) / 2
    return m

n = int(input())
scores = []
for _ in range(n):
    scores.append(int(input()))
result = solution(n, scores)
print(format(result, '.6f'))
