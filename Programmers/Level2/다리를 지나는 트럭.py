from collections import deque


def solution(bridge_length, weight, truck_weights):
    q = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    time = 0

    # 대기 큐가 빌 때까지 시간마다 반복 : 맨 앞 한칸 빼고 0 또는 트럭 넣기
    while q:
        time += 1
        bridge_weight -= bridge.popleft()

        if bridge_weight + q[0] <= weight:
            pop_truck = q.popleft()
            bridge.append(pop_truck)
            bridge_weight += pop_truck
        else:
            bridge.append(0)

    # 대기 큐가 비고 나면 : 다리 위에 트럭 없을 때까지 한칸씩 빼면서 시간 카운트
    while bridge_weight > 0:
        time += 1
        bridge_weight -= bridge.popleft()

    return time
