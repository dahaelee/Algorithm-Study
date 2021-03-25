def solution(participant, completion):
    dict = {}
    for p in participant:
        dict[p] = 0

    # 참가자를 하나씩 확인하면서
    # 완주자 목록에 있으면 완주자 목록에서 제거(동명이인때문), 없으면 value값 1로 변경
    for p in dict:
        if p in completion:
            completion.remove(p)
        else:
            dict[p] = 1

    print(dict)

    return