def solution(skill, skill_trees):
    cnt = 0

    p = []
    for i in range(len(skill) + 1):
        p.append(skill[:i])

    for st in skill_trees:
        s = ''.join([x for x in st if x in skill])

        if s in p:
            cnt += 1

    return cnt
