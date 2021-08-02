class Solution:
    def binary_search(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i, n in enumerate(nums):
            if n in index_map:
                index_map[n].append(i)
            else:
                index_map[n] = [i]

        nums.sort()

        for i in range(len(nums)):
            target1, target2 = nums[i], target - nums[i]
            if self.binary_search(nums, target2, i + 1, len(nums) - 1):
                if target1 == target2:
                    return [index_map[target1][0], index_map[target1][1]]
                else:
                    return [index_map[target1][0], index_map[target2][0]]