def solution(n, k, words, letters):
    result = []

    words.sort()
    count = [0] * k

    for l in letters:
        p = []  # 앞글자가 같은 단어 후보들의 words 리스트에서의 인덱스들
        for i in range(k):
            if l == words[i][0]:
                p.append(i)

        idx = p[0]
        for i in range(1, len(p)):
            if count[p[i]] < count[p[i - 1]]:
                idx = p[i]

        result.append(words[idx])
        count[idx] += 1

    return result

k, n = map(int, input().split())
words = []
letters = []

for _ in range(k):
    words.append(input())
for _ in range(n):
    letters.append(input())

result = solution(n, k, words, letters)
for x in result:
    print(x)
