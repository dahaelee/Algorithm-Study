def solution(s):
    pn = s.count('p') + s.count('P')
    yn = s.count('y') + s.count('Y')

    return pn == yn
