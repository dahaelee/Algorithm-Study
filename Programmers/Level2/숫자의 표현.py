# n에서 m(시작값)*k(개수)를 뺀 값이 1+2+...+(k-1) 이면 OK
# 즉, n에서 1+2+...+(k-1)를 뺀 값을 k로 나눠서 나누어 떨어지면 OK

def solution(n):
    answer = 0

    for k in range(1, n):
        s = (k - 1) * k / 2
        if (n - s) % k == 0 and (n - s) // k > 0:
            answer += 1

    return answer
