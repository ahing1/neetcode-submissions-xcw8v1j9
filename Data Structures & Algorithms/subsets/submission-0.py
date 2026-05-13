class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            # base case at leaf
            if i == len(nums):
                res.append(path[:]) #creates snapshot copy. if regular path whenever you append and pop path those values change in res too
                return
            
            # decision 1: include nums[i]
            path.append(nums[i]) #choose
            backtrack(i+1, path) #explore
            path.pop() #undo

            # decision 2: skip nums[i]
            backtrack(i+1, path)
        
        backtrack(0, [])
        return res
            
