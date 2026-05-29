class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(i, path, curSum):

            if curSum == target:
                res.append(path.copy())
                return
            
            if curSum > target or i >= len(nums):
                return
            
            path.append(nums[i])
            backtrack(i, path, curSum + nums[i])
            path.pop()

            backtrack(i+1, path, curSum)

        backtrack(0, [], 0)
        return res