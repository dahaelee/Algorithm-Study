def solution(absolutes, signs):
    answer = 0

    # for x in zip(absolutes, signs):
    #     answer += x[0] if x[1] else -x[0]
    #
    # return answer

    arr = [a if s else -a for a, s in zip(absolutes, signs)]
    return sum(arr)