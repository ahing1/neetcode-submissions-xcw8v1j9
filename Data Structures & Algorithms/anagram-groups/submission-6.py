class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        hmap = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                freq[i] += 1
            hmap[tuple(freq)].append(s)

        for v in hmap.values():
            res.append(v)
        
        return res
                