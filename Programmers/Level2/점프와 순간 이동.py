# 1이 될때까지 2로 나누면서 나머지가 있을 때만 +1
# = 2진법으로 변환한 뒤 1의 개수

def solution(n):
    return bin(n).count('1')
