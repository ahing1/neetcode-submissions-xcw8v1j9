class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            if nums[l] == target:
                return l
            elif nums[l] < target:
                l += 1
            else:
                r -= 1
        return -1
