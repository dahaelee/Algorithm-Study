import re


def solution(dartResult):
    region = {'S': 1, 'D': 2, 'T': 3}
    results = re.findall('(\d+)([SDT])([*#]?)', dartResult)
    scores = []

    for i, r in enumerate(results):
        scores.append(int(r[0]) ** region[r[1]])

        # 스타상 또는 아차상이 존재한다면
        if r[2] != '':
            if r[2] == '*':
                scores[i] *= 2
                if len(scores) > 1:
                    scores[i - 1] *= 2
            else:
                scores[i] *= -1

    return sum(scores)
