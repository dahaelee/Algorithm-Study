array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 앞에서부터 0번, 1번... 자리들이 있고 그 자리에 누가 올지 찾는다고 생각

for i in range(len(array)): # i는 자리
    min_index = i # 현재 가장 작은 원소의 인덱스 (0부터 시작해서 1씩 증가)
    for j in range(i+1, len(array)): # 가장 작은 원소 바로 다음부터 끝까지의 원소들 중
        if array[min_index] > array[j]: # 가장 작은 원소보다 작으면
            min_index = j # 가장 작은 원소를 갱신
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)
