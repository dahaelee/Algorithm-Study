def solution(arr, n):
    start = 0
    end = n - 1
    cnt = 0

    while start < end:
        if arr[start] == arr[end]:
            start += 1
            end -= 1

        elif arr[start] < arr[end]:
            arr[start + 1] = arr[start] + arr[start + 1]
            cnt += 1
            start += 1

        else:
            arr[end - 1] = arr[end] + arr[end - 1]
            cnt += 1
            end -= 1

    return cnt

n = int(input())
arr = list(map(int, input().split()))

result = solution(arr, n)
print(result)
