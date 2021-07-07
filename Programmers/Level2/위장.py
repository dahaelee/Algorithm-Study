def solution(clothes):
    dic = {}

    for x in clothes:
        if x[1] in dic:
            dic[x[1]] += 1
        else:
            dic[x[1]] = 1

    # itertools.combinations 쓰면 시간 초과
    # solution : (옷개수 + 안입음1) * ... * (옷개수 + 안입음1) - 아무것도안입음1
    answer = 1

    for k in dic:
        answer *= (dic[k] + 1)

    return answer - 1
