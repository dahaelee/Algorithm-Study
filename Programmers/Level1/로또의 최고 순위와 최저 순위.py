def solution(lottos, win_nums):
    cnt = 0

    for x in lottos:
        if x in win_nums:
            cnt += 1

    # mx = 7 - (cnt + lottos.count(0)) if (cnt + lottos.count(0)) > 0 else 6
    # mn = 7 - cnt if cnt > 0 else 6
    #
    # answer = [mx, mn]
    # return answer

    rank = [6, 6, 5, 4, 3, 2, 1]

    return [rank[cnt + lottos.count(0)], rank[cnt]]
