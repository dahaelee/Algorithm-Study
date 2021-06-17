def solution(s):
    brackets = list(s)
    stack = []
    answer = True

    for b in brackets:
        if b == '(':
            stack.append(b)
        else:
            if len(stack) == 0:  # 스택이 비어 있으면
                answer = False
            elif stack[-1] == b:  # 스택 top이 닫는 괄호이면
                answer = False
            else:
                stack.pop()

    # 마지막에 스택이 비어 있지 않으면
    if len(stack) != 0:
        answer = False

    return answer
