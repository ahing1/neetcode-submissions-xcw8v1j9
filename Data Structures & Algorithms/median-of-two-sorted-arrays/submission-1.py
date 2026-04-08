class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A): #get smaller array why?
            A, B = B, A
        
        m, n = len(A), len(B)
        l, r = 0, len(A)
        total = m + n
        half = total // 2

        while True:
            i = l + ((r - l) // 2) #A
            j = half - i

            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < m else float('inf')
            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < n else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2 == 1:
                    return min(Aright, Bright)
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


                
