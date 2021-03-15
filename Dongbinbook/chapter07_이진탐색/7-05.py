def search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
stock = list(map(int, input().split()))
stock.sort()
m = int(input())
req = list(map(int, input().split()))

for i in req:
    result = search(stock, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
