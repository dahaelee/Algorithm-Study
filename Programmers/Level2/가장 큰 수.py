def solution(numbers):
    # numbers를 string 리스트로 변환
    numbers = list(map(str, numbers))

    # ex. 6, 10, 2 -> 666, 101010, 222 라는 문자열들을 정렬하는 것. 숫자 X
    # 원소는 1000 이하이므로 최소 3번 반복해줘야 함.
    numbers.sort(key=lambda x: x * 3, reverse=True)

    # 000 같은 경우 0으로 바꾸기 위해 int로 변환했다가 다시 str로 변환
    return str(int(''.join(numbers)))
