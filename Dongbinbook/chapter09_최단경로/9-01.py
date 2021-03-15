import sys
input = sys.stdin.readline # 치환
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    # 노드 a에서 노드 b로 가는 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드 인덱스
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]: # j는 (노드, 거리) 튜플
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node() # 현재 최단 거리가 가장 짧은 노드를
        visited[now] = True # 방문 처리하고
        for j in graph[now]: # 그 노드와 인접한 노드들에 대하여 반복
            cost = distance[now] + j[1] # 현재 노드를 거쳐서 이동하는 거리를 계산해서
            if cost < distance[j[0]]: # 그게 더 짧으면 최단거리 갱신
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
