from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for r in range(len(nums)):
            
            if dq and dq[0] < r - k + 1: #expired indices removal
                dq.popleft()
            
            while dq and nums[r] > nums[dq[-1]]: #dominance removal
                dq.pop()
            
            dq.append(r) #add current index
            
            if r >= k-1:
                res.append(nums[dq[0]])
        
        return res


