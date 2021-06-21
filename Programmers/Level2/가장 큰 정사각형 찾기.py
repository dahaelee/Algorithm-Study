def solution(board):
    answer = 0

    # (1,1)부터 탐색
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                # 1이면 (왼, 위, 왼위 중 최소값 + 1)로 갱신
                # 세 값이 모두 같아야 거기서 1 증가하므로, 가능한 가장 큰 정사각형의 변 길이가 됨
                board[i][j] = min([board[i][j - 1], board[i - 1][j], board[i - 1][j - 1]]) + 1

    return max([max(x) for x in board]) ** 2
