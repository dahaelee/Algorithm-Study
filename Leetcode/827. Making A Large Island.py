from collections import deque


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def get_valid_next(x, y):
            valid = []

            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    valid.append((nx, ny))

            return valid

        def bfs(x, y, island):
            q = deque()

            q.append((x, y))
            grid[x][y] = island
            area = 1

            while q:
                x, y = q.popleft()

                for nx, ny in get_valid_next(x, y):
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = island
                        area += 1
                        q.append((nx, ny))

            return area

        # 전체 0이거나 전체 1인 경우 먼저 거르기
        total_sum = 0
        for row in grid:
            total_sum += sum(row)

        if total_sum == 0:
            return 1
        elif total_sum == n ** 2:
            return n ** 2

        # 모든 연결된 섬 플러드필, 섬에 들어가는 지점을 섬 번호로 변경
        island = 2
        areas = {}

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    areas[island] = bfs(i, j, island)
                    island += 1

        # 0이면 인접한 섬끼리 더해주면서 최대값 갱신
        answer = 1
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    near_islands = []

                    for nx, ny in get_valid_next(x, y):
                        if grid[nx][ny] > 1:
                            near_islands.append(grid[nx][ny])

                    if near_islands:
                        near_islands = list(set(near_islands))
                        near_areas = [areas[island] for island in near_islands]
                        answer = max(answer, sum(near_areas) + 1)

        return answer
