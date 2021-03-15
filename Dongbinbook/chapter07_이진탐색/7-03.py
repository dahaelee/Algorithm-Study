def search(array, target, start, end):
    if start > end:
        return None

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
