def solution(a, b):
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    # (sum(m[:a - 1]) + b - 1) : 1월 1일부터 a월 b일까지의 일수
    return d[(sum(m[:a - 1]) + b - 1) % 7]
