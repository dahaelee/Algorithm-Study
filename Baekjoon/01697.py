from collections import deque

n, k = map(int, input().split())

queue = deque([n])
dist = [-1] * 100001 # 거리 리스트를 -1로 초기화
dist[n] = 0 # 시작점의 거리는 0

while queue:
    v = queue.popleft()

    # 큐에서 pop한 값이 k이면 끝
    if v == k:
        break

    vns = [v - 1, v + 1, v * 2]

    for vn in vns:
        # 범위를 벗어나면 중단.
        if vn < 0 or vn > 100000:
            continue

        # 여기서 visited[vn]을 확인해야 하기 때문에 vn의 범위 체크를 for문 안에 넣은 것.
        # 벗어난 경우 큐에 넣을지 체크부터를 안하도롣.
        if dist[vn] == -1:
            queue.append(vn)
            dist[vn] = dist[v] + 1

print(dist[k])
