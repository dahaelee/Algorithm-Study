n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j = list(map(int, input().split()))
    graph[i].append(j)
    graph[j].append(i)

affected = [False] * (n + 1)
visited = [False] * (n + 1)

def dfs(x):
    # 이미 방문 상태면 리턴
    if visited[x]:
        return

    # 방문하지 않은 노드면 방문처리하고
    else:
        visited[x] = True

        # 감염시키고
        affected[x] = True

        # 인접한 노드들에 대해 재귀호출
        for c in graph[x]:
            dfs(c)

dfs(1)
print(affected.count(True) - 1)
