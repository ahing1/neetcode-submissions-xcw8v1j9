class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(open, close, cur):

            if open == n and close == n:
                res.append(cur)
                return

            if open < n:
                backtrack(open + 1, close, cur + "(")
            
            if close < open:
                backtrack(open, close + 1, cur + ")")
        
        backtrack(0, 0, "")
        return res
            