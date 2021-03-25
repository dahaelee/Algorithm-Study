def solution(participant, completion):
    for p in participant:
        if p in completion:
            completion.remove(p)
        else:
            return p
