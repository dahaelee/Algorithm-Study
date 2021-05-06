def solution(s):
    words = s.split(' ')
    nwords = []

    for word in words:
        nword = ""
        for i, c in enumerate(word):
            nword += c.upper() if i % 2 == 0 else c.lower()
        nwords.append(nword)

    answer = ' '.join(nwords)
    return answer
