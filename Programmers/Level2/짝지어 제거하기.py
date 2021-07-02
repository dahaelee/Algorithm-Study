# 문자열이 대칭 형태의 반복이면 짝지어 제거 가능 -> 스택으로 검사 (like 괄호검사)

def solution(s):
    alphas = list(s)
    stack = []

    # alphas에서 pop한 글자가 stack의 top과 같으면 둘다 제거, 다르면 stack에 append
    while alphas:
        a = alphas.pop()

        if stack:
            if a == stack[-1]:
                stack.pop()
            else:
                stack.append(a)
        else:
            stack.append(a)

    # alphas가 끝났을 때 stack에 남은 게 없으면 ok
    return 1 if not stack else 0
