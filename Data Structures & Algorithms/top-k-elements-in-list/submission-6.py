import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        max_heap = []
        for n, v in freq.items():
            heapq.heappush(max_heap, (-v, n))

        for _ in range(k):
            v, n = heapq.heappop(max_heap)
            res.append(n)
        
        return res
