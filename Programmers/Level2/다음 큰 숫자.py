def solution(n):
    c = bin(n).count('1')

    while True:
        n += 1
        if bin(n).count('1') == c:
            answer = n
            break

    return answer
