class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, curSum):
            if curSum == target:
                res.append(path.copy())
                return
            
            if start == len(candidates) or curSum > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                curSum += candidates[i]
                backtrack(i + 1, path, curSum)
                curSum -= candidates[i]
                path.pop()
        
        candidates.sort()
        backtrack(0, [], 0)
        return res