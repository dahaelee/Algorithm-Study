n = int(input())

array = []

for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

# 라이브러리를 안 쓰고 푼다면
# 성적의 경우 데이터 범주가 0~100으로 한정적이고,
# 동일한 값을 가지는 데이터가 여러개 등장하기 때문에 계수 정렬이 유리함

count = [[] for _ in range(101)]
sorted_array = []

for i in range(len(array)):
    count[array[i][1]].append(array[i][0])

for i in range(len(count)):
    for j in range(len(count[i])):
        sorted_array.append((count[i][j], i))

print(count)
print(sorted_array)

for i in sorted_array:
    print(i[0], end=' ')

'''
# 그냥 라이브러리+람다함수 사용
array = sorted(array, key=lambda x: x[1])

for i in array:
    print(i[0], end=' ')
'''