class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        res = 0

        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = i
            else:
                l = max(l, seen[s[i]] + 1)

            seen[s[i]] = i
            res = max(res, i - l + 1)
        
        return res