class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        res = []

        for word in strs:
            ana = [0] * 26
            for c in word:
                i = ord(c) - ord('a')
                ana[i] += 1
            
            freq[tuple(ana)].append(word)

        for v in freq.values():
            res.append(v)
        
        return res