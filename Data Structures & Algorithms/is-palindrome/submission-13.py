class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s) - 1
        alphanumeric = "qwertyuiopasdfghjklzxcvbnm1234567890"
        s = s.lower().strip()

        while l < r:
            while l < r and s[l] not in alphanumeric:
                l += 1
            while r > l and s[r] not in alphanumeric:
                r -= 1
            
            if s[l] != s[r]:
                return False
            
            l, r = l + 1, r - 1
        
        return True