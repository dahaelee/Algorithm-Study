# 퀵 정렬

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개 남으면 종료
        return

    pivot = start
    left = start + 1
    right = end

    # 엇갈릴 때까지 현재 피벗을 기준으로 피벗보다 큰 원소, 작은 원소 찾아 반복
    while left <= right:
        while left <= end and array[left] <= array[pivot]: # 피벗보다 큰 원소를 찾을 때까지
            left += 1
        while right > start and array[right] >= array[pivot]: # 피벗보다 작은 원소를 찾을 때까지
            right -= 1

        if left > right: # 엇갈렸다면
            array[right], array[pivot] = array[pivot], array[right] # 작은 원소와 피벗을 교체
        else: # 엇갈리지 않았다면
            array[right], array[left] = array[left], array[right] # 작은 원소와 큰 원소를 교체

    # 여기까지 하면 엇갈려서 right이 새 피벗이 된 상태. 그 기준으로 분할해서 왼쪽과 오른쪽에 각각 정렬 수행.
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
