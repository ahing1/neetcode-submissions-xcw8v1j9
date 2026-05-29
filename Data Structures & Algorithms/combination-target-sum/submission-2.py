class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()

        def backtrack(i, path, curSum):

            if curSum == target:
                res.append(path.copy())
                return
            
            for j in range(i, len(nums)):
                if curSum + nums[j] > target:
                    return
                
                path.append(nums[j])
                backtrack(j, path, curSum + nums[j])
                path.pop()
            

        backtrack(0, [], 0)
        return res