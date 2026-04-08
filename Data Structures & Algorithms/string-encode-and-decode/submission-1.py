class Solution:

    def encode(self, strs: List[str]) -> str:
        len_of_words = [len(s) for s in strs]
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i != len(s):
            n = ""
            while s[i] != "#":
                n += s[i]
                i += 1
            n = int(n)
            j = i+1
            temp = ""
            for _ in range(n):
                temp += s[j]
                j += 1
            i = j
            res.append(temp)
        return res