class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dic = collections.defaultdict(int)
        for i, x in enumerate(sorted(arr)):
            dic[x] += 1

        for x in dic:
            if dic[x] == 0:  # 이미 0개면 패스
                continue

            target = x / 2 if x < 0 else 2 * x  # 음수면 반값, 양수면 두배값 찾기

            if dic.get(target) and dic[target] >= dic[x]:
                dic[target] -= dic[x]
                dic[x] = 0
            else:
                return False

        return True
