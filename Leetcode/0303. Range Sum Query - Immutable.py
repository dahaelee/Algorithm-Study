class NumArray:
    def __init__(self, nums: List[int]):
        nums = [0] + nums

        for i in range(len(nums)):
            nums[i] += nums[i - 1]

        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right + 1] - self.nums[left]
