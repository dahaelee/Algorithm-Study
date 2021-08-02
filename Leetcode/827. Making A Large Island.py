from collections import deque


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def check(x, y):
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                yield nx, ny

        def bfs(x, y, island):
            q = deque()

            q.append((x, y))
            grid[x][y] = island
            area = 1

            while q:
                x, y = q.popleft()

                for nx, ny in check(x, y):
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = island
                        area += 1
                        q.append((nx, ny))

            return area

        # 모든 연결된 섬 플러드필, 섬에 들어가는 지점을 섬 번호로 변경
        island = 2
        areas = {}
        has_zero = False

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    areas[island] = bfs(i, j, island)
                    island += 1

        # 0이면 인접한 섬끼리 더해주면서 최대값 갱신, 이때 인접한 섬이 한 섬일 경우 고려
        answer = 1
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    has_zero = True
                    near_island = []

                    for nx, ny in check(x, y):
                        if grid[nx][ny] > 1:
                            near_island.append(grid[nx][ny])

                    if near_island:
                        near_island = list(set(near_island))
                        near_area = [areas[x] for x in near_island]
                        answer = max(answer, sum(near_area) + 1)

        return answer if has_zero else n ** 2
