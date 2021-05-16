'''
정확도는 통과하지만 테케 하나에서 시간초과가 나는 풀이
이중 for문은 최대한 피하고, 불가피할 때는 시간복잡도를 체크하자

def solution(N, stages):
    stry = [0] * N  # 스테이지에 도전한 사용자 수
    sclear = [0] * N  # 스테이지를 클리어한 사용자 수
    fail = [0] * N  # 스테이지의 실패율

    for x in stages:
        s = x - 1 if x > N else x

        for i in range(s):
            stry[i] += 1

        for i in range(x - 1):
            sclear[i] += 1

    for i, t in enumerate(zip(stry, sclear)):
        if t[0]:
            fail[i] = (t[0] - t[1]) / t[0]
        else:
            fail[i] = 0

    a = sorted([x for x in enumerate(fail, start=1)], key=lambda x: x[1], reverse=True)

    return [x[0] for x in a]
'''


def solution(N, stages):
    fail = {}
    users = len(stages)

    # 스테이지마다 실패율 계산
    # 실패율 = 실패한 유저 수 / 도달한 유저 수
    # 1스테이지에서는 도달한 유저 수 = 전체 유저 수
    # 다음 단계에 도달한 유저 수는 실패 유저수를 빼가면서 구함

    for stage in range(1, N + 1):
        if users:
            failed = stages.count(stage)
            fail[stage] = failed / users
            users -= failed

        else:  # 스테이지에 도달한 사람 없으면 실패율 0
            fail[stage] = 0

    return sorted(fail, key=lambda x: fail[x], reverse=True)
