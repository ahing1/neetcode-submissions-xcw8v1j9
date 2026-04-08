class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        res = []

        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
        
        for i in range(k):
            top_freq = max(h, key = h.get)
            res.append(top_freq)
            del h[top_freq]
        
        return res
            

        