# 계수 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * len(array) # 개수를 담을 리스트. 정렬할 리스트에 중복이 없어도 커버할 수 있는 사이즈.

for i in array: # 원소의 값을 인덱스로 해서 count 리스트에 개수 세기
    count[i] += 1

for i in range(len(count)): # count 리스트의 인덱스를 원소값만큼 출력
    for j in range(count[i]): 
        print(i, end=' ')
