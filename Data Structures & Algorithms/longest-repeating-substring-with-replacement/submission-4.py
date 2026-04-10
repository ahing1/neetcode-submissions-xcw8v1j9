class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            # while window is invalid, move left pointer
            while (r - l + 1) - max(count.values()) > k: #window - count of most frequent element = chars that need to be swapped
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        
        return res