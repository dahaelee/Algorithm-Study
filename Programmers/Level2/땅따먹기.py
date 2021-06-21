def solution(land):
    n = len(land)

    # 각 원소값을 (자기 자신 + 이전행에서 같은 열 제외한 최대값) 으로 바꾸면서 모든 행을 탐색
    for i in range(1, n):
        for j in range(0, 4):
            land[i][j] = land[i][j] + max(land[i - 1][:j] + land[i - 1][j + 1:])

        ''' 내부 for문과 동일한 코드
        land[i][0] = land[i][0] + max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] = land[i][1] + max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] = land[i][2] + max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] = land[i][3] + max(land[i-1][0], land[i-1][1], land[i-1][2])
        '''

    # 답은 마지막 행의 최대값
    answer = max(land[-1])

    return answer
