# 주어진 수를 m번 더하되, 같은 인덱스의 수를 k번 초과해 더할 수 X
# 제일큰수k번 + 그다음1번 + 제일큰수k번 + 그다음1번..

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0

nums.sort(reverse=True)
n1 = nums[0]
n2 = nums[1]

while True:
    for _ in range(k):
        if m == 0:
            break
        ans += n1
        m -= 1

    if m == 0:
        break
    ans += n2
    m -= 1

print(ans)

# 수학적으로 풀어보면 수열을 이용
# 가장 큰수가 더해지는 횟수 = int(m/(k+1)*k + m%(k+1))
# 두번째 큰수가 더해지는 횟수 = m - 위의수