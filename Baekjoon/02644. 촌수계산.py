from collections import deque

n = int(input())
target1, target2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

queue = deque()
visited = [False] * (len(graph))
distance = [-1] * (len(graph))

queue.append(target1)
distance[target1] = 0
answer = -1

while queue:
    t = queue.popleft()

    if t == target2:
        answer = distance[t]
        break

    if not visited[t]:
        visited[t] = True
        for k in graph[t]:
            distance[k] = distance[t] + 1
            queue.append(k)

print(answer)
