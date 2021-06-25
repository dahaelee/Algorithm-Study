def solution(n, words):
    answer = []

    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1] or words[i] in words[:i]:
            p = i % n + 1  # 탈락자의 번호
            t = i // n + 1  # 몇 번째 차례
            return [p, t]

    return [0, 0]
