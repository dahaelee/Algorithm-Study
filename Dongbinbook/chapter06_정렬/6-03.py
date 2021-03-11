# 삽입 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 앞에서부터 0번, 1번... 원소들이 있고 그 원소가 어디에 갈지 찾는다고 생각

for i in range(len(array)): # i는 원소
    for j in range(i, 0, -1): # i번째 원소부터 제일 앞까지 탐색하면서
        if array[j-1] > array[j]: # 왼쪽 원소가 더 크면
            array[j], array[j-1] = array[j-1], array[j] # 스와프해 한칸씩 왼쪽으로 이동
        else: # 왼쪽 원소가 더 작은걸 만날 때까지
            break

print(array)

