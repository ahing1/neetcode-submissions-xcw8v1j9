class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = nums[i-1] * output[i-1]

        right_prod = 1
        for i in range(len(nums) - 1, -1 , -1):
            output[i] *= right_prod
            right_prod *= nums[i]
        return output