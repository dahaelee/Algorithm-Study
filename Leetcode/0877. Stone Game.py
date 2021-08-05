class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        left, right = 0, n - 1
        diff = 0  # 알렉스 - 리

        while left < right:
            # 알렉스 순서
            if piles[left] < piles[right]:
                diff += piles[right]
                right -= 1
            else:
                diff += piles[left]
                left += 1

            # 리 순서
            if piles[left] < piles[right]:
                diff -= piles[left]
                left += 1
            else:
                diff += piles[right]
                right -= 1

        return diff > 0
