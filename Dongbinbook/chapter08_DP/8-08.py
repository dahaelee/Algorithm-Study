# 화폐 단위 k에 대한 점화식 a(i) = min(a(i), a(i-1) + k) 를 모든 화폐 단위에 대하여 적용

n, m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))

d = [10001] * (m+1)
d[0] = 0

# 모든 화폐 단위에 대하여, 모든 금액에 대하여 반복
for i in range(n):
    # i는 화폐 단위, j는 금액을 의미.
    for j in range(money[i], m + 1): # 화폐단위~금액에 대하여 반복
        if d[j - money[i]] != 10001: # 금액-화폐단위 만들 수 있으면
            d[j] = min(d[j], d[j - money[i]] + 1) # 그거+1 이랑 지금거 중에 작은거

print(d[m] if d[m] != 10001 else -1)
