def solution(n, computers):
    graph = [[] for _ in range(n + 1)]

    for i, c in enumerate(computers):
        for j, v in enumerate(c):
            if i != j and v == 1:
                graph[i + 1].append(j + 1)
                graph[j + 1].append(i + 1)

    visited = [False] * (n + 1)
    cnt = 0

    def dfs(x):
        # 이미 방문한 노드면 리턴
        if visited[x]:
            return False

        visited[x] = True
        for n in graph[x]:
            dfs(n)

        return True

    for i in range(1, n + 1):
        if dfs(i):
            cnt += 1

    return cnt
