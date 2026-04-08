class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                chars[i] += 1
            
            freq[tuple(chars)].append(s)
        
        res = []
        for val in freq.values():
            res.append(list(val))
        
        return res