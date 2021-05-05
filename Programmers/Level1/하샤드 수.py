def solution(x):
    answer = False

    # x의 자릿수의 합 구하기
    s = sum([int(i) for i in str(x)])

    if x % s == 0:
        answer = True
    return answer
