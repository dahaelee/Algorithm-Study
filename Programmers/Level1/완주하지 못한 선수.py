def solution(participant, completion):
    dic = {}

    # 여기서 count 함수를 쓰면 시간 초과로 효율성 탈락
    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1

    for c in completion:
        dic[c] -= 1

    for p in dic:
        if dic[p] > 0:
            return p

'''
# 아래 코드는 정확성은 100프로지만 효율성 검사를 통과하지 못함.
# remove(n)의 시간복잡도가 O(n)이라 for문 안에 들어가면 O(n^2)이 되기 때문

def solution(participant, completion):
    for p in participant:
        if p in completion:
            completion.remove(p)
        else:
            return p
'''
