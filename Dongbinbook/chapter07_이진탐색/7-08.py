n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in array:
        if x > mid:
            total += x - mid
    if total < m: # 필요한 것보다 덜 잘랐을 때. 자르는 지점을 왼쪽으로
        end = mid - 1
    else : # 필요한 것보다 더 잘랐을 때. 자르는 지점을 오른쪽으로
        result = mid # 답을 지금 중간값으로 갱신
        start = mid + 1

print(result)
