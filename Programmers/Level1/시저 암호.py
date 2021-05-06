def push(x, n):
    # 한칸씩 밀면서 확인
    while n > 0:
        if x == 'Z':
            x = 'A'
        elif x == 'z':
            x = 'a'
        else:
            x = chr(ord(x) + 1)
        n -= 1
    return x


def solution(s, n):
    a = list(s)

    for i in range(len(a)):
        if a[i] == ' ':
            continue
        else:
            a[i] = push(a[i], n)

    return ''.join(a)