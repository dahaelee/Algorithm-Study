def solution(arr, divisor):
    answer = sorted([x for x in arr if x % divisor == 0])
    return answer if len(answer) else [-1]
