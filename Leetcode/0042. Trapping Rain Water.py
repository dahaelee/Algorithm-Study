class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        water = 0

        for i in range(1, len(height) - 1):
            left_max = max(height[:i])
            right_max = max(height[i + 1:])
            min_bar = min(left_max, right_max)

            if height[i] < min_bar:
                water += (min_bar - height[i])

        return water
