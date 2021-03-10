from collections import deque

n, m, v = map(int, input().split())

# 한 행마다 숫자 두개 바꿔서 append 두번씩 해줘야함.
graph = [[] for _ in range(n + 1)] # 0번째거 포함해서 정점보다 하나 많게 빈 리스트의 이중리스트
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = deque()

    queue.append(start)
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 방문 가능한 노드가 여러개면 작은것부터이므로 오름차순정렬
for each in graph:
    each.sort()

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
