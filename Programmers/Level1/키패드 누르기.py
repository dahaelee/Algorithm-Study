def solution(numbers, hand):
    answer = ''

    left_now = 10
    right_now = 12

    for x in numbers:
        x = 11 if x == 0 else x  # 0이면 11로 바꿔주기

        if x in [1, 4, 7]:
            answer += 'L'
            left_now = x
        elif x in [3, 6, 9]:
            answer += 'R'
            right_now = x
        else:
            ldis = sum(divmod(abs(x - left_now), 3))
            rdis = sum(divmod(abs(x - right_now), 3))

            if ldis < rdis:
                answer += 'L'
                left_now = x
            elif ldis > rdis:
                answer += 'R'
                right_now = x
            else:
                if hand == 'left':
                    answer += 'L'
                    left_now = x
                else:
                    answer += 'R'
                    right_now = x
    return answer
