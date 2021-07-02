def solution(citations):
    citations.sort(reverse=True)
    index = 0

    for i in range(len(citations)):
        # 인용 횟수 h >= h번 이상 인용된 논문 수 이면, 논문 수로 인덱스 갱신
        if citations[i] >= i + 1:
            index = i + 1

    return index
