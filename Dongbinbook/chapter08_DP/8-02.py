d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1

    # 이미 계산한 적 있는 문제라면 리스트에 있는 그대로 반환
    if d[x] != 0:
        return d[x]

    # 아직 계산한 적 없는 문제라면 값을 리스트에 기록하고 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
