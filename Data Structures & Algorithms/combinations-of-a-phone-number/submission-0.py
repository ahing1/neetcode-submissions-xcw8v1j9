class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
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

        res = []

        if digits == "":
            return []

        def backtrack(i, path):

            if i == len(digits):
                res.append("".join(path.copy()))
                return
            
            for letter in letters[digits[i]]:
                path.append(letter)
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return res