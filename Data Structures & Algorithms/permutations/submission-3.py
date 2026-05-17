class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        visited = [False] * len(nums)

        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
            
            for i in range(len(nums)):
                if visited[i] == False:
                    perm.append(nums[i])
                    visited[i] = True
                    backtrack(perm)
                    perm.pop()
                    visited[i] = False
        
        backtrack([])
        return res