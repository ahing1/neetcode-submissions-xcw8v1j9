class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            freq = [0] * 26
            for c in word:
                i = ord(c) - ord('a')
                freq[i] += 1
            key = tuple(freq)
            groups[key].append(word)
        
        return list(groups.values())