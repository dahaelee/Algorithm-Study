# 재귀함수 종료 예제

def recursive(i):
    if i == 10:
        return
    print(f'{i}번째 재귀함수에서 {i+1}번째 재귀함수를 호출')
    recursive(i+1)
    print(f'{i}번째 재귀함수 종료')

recursive(1)