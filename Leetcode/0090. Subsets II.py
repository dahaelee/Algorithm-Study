from itertools import combinations as com


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()

        for i in range(len(nums) + 1):
            subsets += com(nums, i)

        return list(map(list, set(subsets)))

'''
# itertools 사용하지 않고 섭셋에 원소 하나씩 더하는 방법
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set([()])
        nums.sort()

        for num in nums:
            for subset in list(subsets):
                subsets.add(subset + (num,))

        return list(map(list, subsets))
'''
