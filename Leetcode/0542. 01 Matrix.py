from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])

        q = deque()
        dist = [[10000] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if mat[i][j] is 0:
                    dist[i][j] = 0
                    q.append((i, j))

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= row or ny < 0 or ny >= col:
                    continue

                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        return dist
