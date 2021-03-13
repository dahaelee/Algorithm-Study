def search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    # 중간값이 타켓보다 크면 왼쪽 확인
    elif array[mid] > target:
        return search(array, target, start, mid-1)

    # 중간값이 타겟보다 작으면 오른쪽 확인
    else:
        return search(array, target, mid+1, end)

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)
