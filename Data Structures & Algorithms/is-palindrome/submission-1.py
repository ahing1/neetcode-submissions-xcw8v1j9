class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = "qwertyuiopasdfghjklzxcvbnm1234567890"
        l, r = 0, len(s) - 1

        while l < r:
            if s[l].lower() not in alphanumeric:
                l += 1
                continue
            if s[r].lower() not in alphanumeric:
                r -= 1
                continue
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True