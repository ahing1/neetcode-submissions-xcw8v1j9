class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        for i in range(1, n):
            output[i] = nums[i - 1] * output[i - 1]
        
        rightProd = 1
        for i in range(n - 1, -1, -1):
            output[i] *= rightProd
            rightProd *= nums[i]
        
        return output