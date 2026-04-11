class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1Count = {}
        for c in s1:
            if c not in s1Count:
                s1Count[c] = 1
            else:
                s1Count[c] += 1
        

        s2Count = {}
        window = s2[:len(s1)]
        for c in window:
            if c not in s2Count:
                s2Count[c] = 1
            else:
                s2Count[c] += 1
        
        l = 0
        r = len(s1)
        while r < len(s2):

            if s2Count == s1Count:
                return True

            s2Count[s2[r]] = 1 + s2Count.get(s2[r], 0)
            s2Count[s2[l]] = s2Count.get(s2[l]) - 1
            if s2Count[s2[l]] == 0:
                del s2Count[s2[l]]

            r += 1
            l += 1


        return True if s1Count == s2Count else False
            


