def solution(board, moves):
    nboard = [[] for _ in range(len(board))]
    stack = []
    answer = 0

    for r in board:
        for i, x in enumerate(r):
            if x == 0:
                continue
            else:
                nboard[i].append(x)

    for i in moves:
        if nboard[i - 1]:
            x = nboard[i - 1].pop(0)  # 해당 열에서 제일 위에 있는 인형

            # 스택이 비어있으면 바로 넣고, 아니면 비교
            if not stack:
                stack.append(x)
            else:
                if x == stack[-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(x)

    return answer
