class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, path, curSum):
            if curSum == target:
                res.append(path[:])
                return
            
            if curSum > target or i == len(nums):
                return
            
            # choose num
            curSum += nums[i]
            path.append(nums[i])
            backtrack(i, path, curSum)
            path.pop()
            curSum -= nums[i]

            #  skip
            backtrack(i + 1, path, curSum)
        
        backtrack(0, [], 0)
        return res