class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        # k e [l, r]
        
        while l <= r:
            k = l + ((r - l) // 2) #k is a value not a index
            hours = sum((p+k-1)//k for p in piles)

            if hours <= h:
                r = k - 1 # boundary update ex: [1, 5]
            else:
                l = k + 1

        return l