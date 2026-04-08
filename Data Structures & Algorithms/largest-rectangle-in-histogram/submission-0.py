class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lstack = []
        rstack = []
        n = len(heights)
        L = [-1] * n
        R = [n] * n
        max_area = 0

        for i in range(len(heights)):
            while lstack and heights[lstack[-1]] >= heights[i]:
                lstack.pop()
            if not lstack:
                L[i] = -1
            else:
                L[i] = lstack[-1]
            lstack.append(i)
        
        for i in range(len(heights) - 1, -1, -1):
            while rstack and heights[rstack[-1]] >= heights[i]:
                rstack.pop()
            if not rstack:
                R[i] = n
            else:
                R[i] = rstack[-1]
            rstack.append(i)
        
        for i in range(len(heights)):
            area_i = heights[i] * (R[i] - L[i] - 1)
            max_area = max(max_area, area_i)
        
        return max_area