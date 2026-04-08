class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(s) < len(t):
            return res
        
        need = {} #freq map of what must be present including duplicates
        have = {} #freq map of the current window in s
        formed = 0 

        for c in t:
            need[c] = need.get(c, 0) + 1
        required = len(need) #num of distinct chars we must satisfy

        l = 0
        best_len = float('inf')
        best_l, best_r = 0, 0
        for r in range(len(s)):
            have[s[r]] = have.get(s[r], 0) + 1

            if s[r] in need and have[s[r]] == need[s[r]]: #meets conditions
                formed += 1
            
            # shrink when valid
            while formed == required:

                if r-l+1 < best_len: #update result before shrinking, shrinking first might break validity
                    best_len = r-l+1
                    best_l = l
                    best_r = r

                have[s[l]] -= 1 #shrink

                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1 #make window invalid
                
                l += 1
        
        return "" if best_len == float('inf') else s[best_l:best_r + 1]