from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for char in s:
                i = ord(char) - ord('a')
                counts[i] += 1
            key = tuple(counts)
            groups[key].append(s)

        return list(groups.values())
        

