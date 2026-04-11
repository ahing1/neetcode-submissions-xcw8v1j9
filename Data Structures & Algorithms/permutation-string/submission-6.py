class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # if len(s1) > len(s2):
        #     return False
        
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
        while r < len(s2): #dont want <= bc then when we try to access the new element below we will get index error on last window

            if s2Count == s1Count: #check if current window is good
                return True

            s2Count[s2[r]] = 1 + s2Count.get(s2[r], 0) #add new element to window
            s2Count[s2[l]] = s2Count.get(s2[l]) - 1 #remove last element from window
            if s2Count[s2[l]] == 0:
                del s2Count[s2[l]] #we want to delete bc even though values is 0 the key still exists in hash map so comparison will fail

            #update window, pointers would be 1 ahead of current window after updating
            r += 1
            l += 1

        return True if s1Count == s2Count else False # check for the last window
            


