def solution(arr):
    res = []

    for x in arr:
        # 첫 원소이거나 or 방금 넣은 거랑 비교해서 다르면 넣기
        if len(res) == 0 or x != res[-1]:
            res.append(x)
    return res
