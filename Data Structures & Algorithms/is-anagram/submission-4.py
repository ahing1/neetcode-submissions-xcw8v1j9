class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_freq = {}
        for c in s:
            if c not in s_freq:
                s_freq[c] = 1
            else:
                s_freq[c] += 1
        
        t_freq = {}
        for c in t:
            if c not in t_freq:
                t_freq[c] = 1
            else:
                t_freq[c] += 1
        
        return s_freq == t_freq