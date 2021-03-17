def solution(s, e, n):
    arr = []
    for i in range(n):
        arr.append((s[i], e[i]))

    arr.sort(key=lambda x: (x[1], x[0]))

    e1 = -1
    e2 = -1
    cnt = 0

    # e1, e2 둘 다 앉을 수 있는 학생은 더 늦게 끝나는 좌석에 앉혀야 함
    # e1을 e2보다 먼저 확인하므로, e2에만 들어갈 수 있는 학생이 나오면 e1에 있는 학생을 e2로 옮기고 e1에 앉히기

    for x in arr:
        if x[0] >= e1:
            e1 = x[1]
            cnt += 1

        elif x[0] >= e2:
            e2 = e1
            e1 = x[1]
            cnt += 1

    return cnt

n = int(input())
s = list(map(int, input().split()))
e = list(map(int, input().split()))

result = solution(s, e, n)
print(result)