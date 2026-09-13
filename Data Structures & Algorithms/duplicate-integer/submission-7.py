class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dupe = set(nums)
        return len(dupe) != len(nums)