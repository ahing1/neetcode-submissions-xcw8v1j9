class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()

        for num in nums:
            dup.add(num)
        
        return len(nums) != len(dup)