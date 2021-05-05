def solution(n):
    # answer = int(''.join(sorted(str(n), reverse=True)))

    arr = list(str(n))
    arr.sort(reverse=True)
    answer = int(''.join(arr))

    return answer
