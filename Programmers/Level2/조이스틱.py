def solution(name):
    chars = list(name)
    cnt = 0

    # 글자 별 조작 횟수 : 위로 이동, 아래로 이동 중 작은 값
    for x in name:
        cnt += min(ord(x) - ord('A'), ord('Z') - ord(x) + 1)

    # 글자 간 이동 횟수
    idx = 0

    while True:
        chars[idx] = 'A'

        if len(chars) - chars.count('A') == 0:
            break

        # 현재 상황에서 왼쪽, 오른쪽 중 A가 어디에 많은지에 따라 결정
        left, right = 1, 1
        while chars[idx - left] == 'A':
            left += 1
        while chars[idx + right] == 'A':
            right += 1

        cnt += left if left < right else right
        idx += -left if left < right else right

    return cnt
