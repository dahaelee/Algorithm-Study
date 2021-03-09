# 나누는 연산을 최대한 많이 해야 횟수가 작다는 정당성

n, k = map(int, input().split())

cnt = 0

while n > 1:
    if n % k == 0:
        n = n//k
        cnt += 1
    else:
        n = n - 1
        cnt += 1

'''
# 수학적으로 풀기

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
'''

print(cnt)
