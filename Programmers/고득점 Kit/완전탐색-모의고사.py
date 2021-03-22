def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0] * 3
    result = []

    # answers에 대하여 i는 인덱스, answer는 값
    for i, answer in enumerate(answers):
        if answer == s1[i % len(s1)]:
            score[0] += 1
        if answer == s2[i % len(s2)]:
            score[1] += 1
        if answer == s3[i % len(s3)]:
            score[2] += 1

    for i in range(3):
        if score[i] == max(score):
            result.append(i + 1)

    return result
