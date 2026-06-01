class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        letters = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        def backtrack(i, path):
            if i == len(digits):
                res.append("".join(path))
                return
            
            for j in range(len(letters[digits[i]])):
                path.append(letters[digits[i]][j])
                backtrack(i+1 ,path)
                path.pop()
        
        if digits == "":
            return []

        backtrack(0, [])
        return res