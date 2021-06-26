def solution(number, k):
    res = [number[0]]

    for n in number[1:]:

        # res에 값이 있고, 마지막 원소가 현재 탐색 원소보다 작고, 제거 횟수 이내일 때
        while res and res[-1] < n and k > 0:
            res.pop()
            k -= 1

        res.append(n)

    # k번 만큼 제거를 못 했을 때
    if k > 0:
        res = res[:-k]

    return ''.join(res)
