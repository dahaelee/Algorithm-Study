def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    print(answer)

    for i in range(len(arr1)):  # arr1의 행
        for j in range(len(arr2[0])):  # arr2의 열
            for k in range(len(arr1[0])):  # arr1의 열이자 arr2의 행
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer
