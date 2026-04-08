class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dupes = set(nums)
        return True if len(nums) != len(no_dupes) else False
         