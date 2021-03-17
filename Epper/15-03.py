def solution(n, m):
    day = 0
    flag = 0

    while n > 0:
        day += 1
        flag += 1

        # m일째 되는 날이면 재고 추가
        if flag == m:
            n += 1
            flag = 0

        n -= 1

    return day

n, m = map(int, input().split())
result = solution(n, m)
print(result)
