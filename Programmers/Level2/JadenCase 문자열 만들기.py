# replace는 일치하는 문자열을 다 치환함. 하나만 바꾸고싶으면 횟수를 인자로 전달해야 함.
# 그렇게 안할거면 list로 만들어서 인덱스로 바꾼다음 다시 join하는 방법.

def solution(s):
    s = s.lower()
    w = s.split(" ")

    for i in range(len(w)):
        if len(w[i]) > 0:
            w[i] = w[i].replace(w[i][0], w[i][0].upper(), 1)

    return " ".join(w)
