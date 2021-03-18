from collections import deque

def solution(n, r, goal, N, R):
    queue = deque()
    indegree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]

    # 인덱스를 노드 번호에 맞추기
    for i in range(len(r)):
        graph[i + 1] = r[i]

    # 진입차수
    for x in graph:
        for i in x:
            indegree[i] += 1

    # 해당 공정까지 완료하는데 걸리는 최대 시간의 리스트
    time = [0] * (N + 1)

    # 진입차수가 0인 공정을 큐에 삽입하고 최대 시간을 해당 공정의 시간으로
    for i in range(1, N + 1):
        if indegree[i] == 0:
            time[i] = n[i - 1] # 리스트 n만 인덱스 안맞아서 맞춰줘야 함
            queue.append(i)

    while queue:  # 큐가 빌 때까지
        now = queue.popleft()

        # 연결되어 있는 노드들의 진입차수에서 1을 빼고, 0이 되면 큐에 삽입
        for i in graph[now]:
            # 최대 시간은 max(지금까지 계산된 시간, 이전 공정까지 걸리는 시간 + 지금 공정 시간)
            time[i] = max(time[i], time[now] + n[i - 1])
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    return time[goal]

N, R = map(int, input().split())
n = list(map(int, input().split()))
r = [[] for _ in range(N - 1)]
for _ in range(R):
    a, b = map(int, input().split())
    r[a - 1].append(b)
goal = int(input())

result = solution(n, r, goal, N, R)
print(result)
