class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # doing binary search on the range of values of k
        # k = [1, max(piles)]

        l = 1
        r = max(piles)

        res = r

        while l <= r:
            k = l + ((r - l) // 2)

            totalTime = 0
            for pile in piles:
                time = math.ceil(pile/k)
                totalTime += time

            if totalTime > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1

            
        
        return res

                