class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_height = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            if area > max_height:
                max_height = area

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1

        return max_height
