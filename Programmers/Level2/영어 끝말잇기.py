def solution(n, words):
    answer = []

    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1] or words[i] in words[:i]:
            q, r = divmod(i + 1, n)
            p = n if r == 0 else r  # 탈락자의 번호
            t = q if r == 0 else q + 1  # 몇 번째 차례
            return [p, t]

    return [0, 0]
