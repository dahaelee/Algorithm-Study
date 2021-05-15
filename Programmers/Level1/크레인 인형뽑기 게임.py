def solution(board, moves):
    answer = 0
    stack = []

    def check(item):
        if len(stack) > 0 and stack[-1] == item:
            stack.pop()
            return 2
        else:
            stack.append(item)
            return 0

    for i in moves:
        for index in range(len(board)):
            if board[index][i - 1] != 0:
                answer += check(board[index][i - 1])
                board[index][i - 1] = 0
                break

    return answer