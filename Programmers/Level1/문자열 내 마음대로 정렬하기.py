def solution(strings, n):
    strings.sort() # 인덱스 n의 문자가 같은 문자열이 여럿일 경우를 대비해 먼저 사전순 정렬
    return sorted(strings, key=lambda x: x[n])
