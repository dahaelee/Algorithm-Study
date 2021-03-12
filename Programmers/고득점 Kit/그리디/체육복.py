def solution(n, lost, reserve):
    # 여벌을 가져온 학생이 도난당한 경우 처리
    for i in range(1, n + 1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)

    # 도난당한 학생 앞뒤에서 빌리고, 빌리면 여벌 없앰
    for i in range(1, n + 1):
        if i in lost:
            if i - 1 in reserve:
                lost.remove(i)
                reserve.remove(i - 1)
            elif i + 1 in reserve:
                lost.remove(i)
                reserve.remove(i + 1)

    answer = n - len(lost)
    return answer