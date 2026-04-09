class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        res = 0

        for num in nums:
            seq = 0
            temp = num
            if temp - 1 not in unique:
                seq = 1
            while temp + 1 in unique:
                seq += 1
                temp += 1
            
            res = max(res, seq)

        return res
