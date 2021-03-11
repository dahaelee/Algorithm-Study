# 수학적으로 풀기

n, k = map(int, input().split())

cnt = 0

while True:
    # n이 k로 나누어질때까지 1 빼는데, 그걸 한번에
    target = (n//k) * k
    cnt += (n-target)
    n = target
    
    if n < k:
        break;
    
    n //= k
    cnt += 1

# 남은 수가 1 될때까지 1씩 빼는 횟수
cnt += (n-1)

print(cnt)
