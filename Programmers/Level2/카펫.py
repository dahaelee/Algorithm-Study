def solution(brown, yellow):
    # yellow의 약수 중에서 조건을 만족하는 값 찾기
    for h in range(1, int((yellow**0.5) + 1)):
        if yellow % h == 0:
            w = yellow // h
            if (w + h) * 2 + 4 == brown:
                return [w + 2, h + 2]
