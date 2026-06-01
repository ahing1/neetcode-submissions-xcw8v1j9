class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        
        def isPalindrone(s):
            return s == s[::-1]
        
        def backtrack(start, path):

            if start == len(s):
                res.append(path.copy())
                return
            
            for i in range(start, len(s)):
                if isPalindrone(s[start:i+1]):
                    path.append(s[start:i+1])
                    backtrack(i + 1, path)
                    path.pop()
            
        backtrack(0, [])
        return res