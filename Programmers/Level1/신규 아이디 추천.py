import re

def solution(new_id):
    st = new_id.lower() # 1단계
    st = re.sub('[^a-z0-9-_.]', '', st) # 2단계
    st = re.sub('\.+', '.', st) # 3단계
    st = re.sub('^[.]|[.]$', '', st) # 4단계
    st = 'a' if len(st) == 0 else st[:15] # 5단계 + 6단계(1)
    st = re.sub('[.]$', '', st) # 6단계(2)
    st += (st[-1] * (3 - len(st))) if len(st) < 3 else '' # 7단계

    return st

'''
def solution(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c

    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계
    if answer == '.':
        answer = ''
    else:
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 5단계
    if len(answer) == 0:
        answer = 'a'

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15] if answer[14] != '.' else answer[:14]

    # 7단계
    while len(answer) < 3:
        answer += answer[-1]

    return answer
'''
