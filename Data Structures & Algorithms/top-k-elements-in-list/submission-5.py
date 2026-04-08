class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in freq.items():
            buckets[val].append(key)

        res = []
        count = 0
        for i in range(len(buckets) - 1, -1 , -1):
            for num in buckets[i]:
                res.append(num)
                count += 1
                if count == k:
                    return res

                    