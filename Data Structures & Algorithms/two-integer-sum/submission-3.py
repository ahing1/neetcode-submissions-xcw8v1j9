class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in h:
                return [h[diff], i]
            else:
                h[num] = i
