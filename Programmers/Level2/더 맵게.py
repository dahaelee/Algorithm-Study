from heapq import *


def solution(scoville, K):
    cnt = 0
    heapify(scoville)

    while scoville[0] < K:  # scoville[0]이 힙의 최솟값
        if len(scoville) <= 1:
            return -1

        n1 = heappop(scoville)
        n2 = heappop(scoville)
        heappush(scoville, n1 + n2 * 2)
        cnt += 1

    return cnt
