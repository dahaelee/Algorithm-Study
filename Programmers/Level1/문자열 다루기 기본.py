def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
    for x in s:
        if x < '0' or x > '9':
            answer = False
    return answer
