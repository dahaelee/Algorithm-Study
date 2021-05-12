'''
def arr_to_map(n, arr):
    m = []
    for x in arr:
        b = []
        while x // 2 > 0:
            b.append(x % 2)
            x = x // 2
        b.append(x % 2)
        for _ in range(n - len(b)):
            b.append(0)
        m.append(list(reversed(b)))
    return m

def solution(n, arr1, arr2):
    map1 = arr_to_map(n, arr1)
    map2 = arr_to_map(n, arr2)

    map3 = []

    for i in range(n):
        s = ''
        for j in range(n):
            s += ' ' if map1[i][j] + map2[i][j] == 0 else '#'
        map3.append(s)

    return map3
'''


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        r = bin(i | j)[2:]  # 합친 지도의 행 = 두 지도의 각 행을 or연산한 후 2진 변환
        r = r.rjust(n, '0')
        r = r.replace('1', '#')
        r = r.replace('0', ' ')
        answer.append(r)
    return answer
