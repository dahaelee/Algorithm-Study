# 특정 노드에 방문한 적 없다면, 상하좌우 중 값이 0이면서 방문하지 않은 노드가 있으면 방문하는 것을 재귀적으로.
# 이것을 모든 노드에 대해 실행. dfs 실행 횟수가 곧 덩어리 개수.

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 범위를 벗어나는 경우 즉시 종료
    if (x < 0 or x >= n or y < 0 or y >= m):
        return False

    # 지금 노드에 방문한 적 없고 0이면 dfs 수행 (0인 칸을 방문하면 1로 바꿔줌으로써 방문 체크)
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상하좌우 전부 재귀 호출
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True

    # 지금 노드가 1이면 종료
    return False

cnt = 0

# 모든 노드에 대해 dfs 수행하고 그 횟수를 카운트
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            cnt += 1

print(cnt)

