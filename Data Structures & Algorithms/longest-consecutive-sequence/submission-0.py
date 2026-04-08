class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        for num in nums:
            seq = 0
            if num-1 not in num_set:
                seq = 1
                while num + seq in num_set:
                    seq += 1
            res = max(res, seq)
        return res