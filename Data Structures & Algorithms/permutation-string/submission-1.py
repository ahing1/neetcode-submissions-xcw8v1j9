class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        for c in s1:
            need[ord(c) - ord('a')] += 1

        # initial window
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if need[i] == window[i]:
                matches += 1

        if matches == 26:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            idx_in = ord(s2[r]) - ord('a')
            idx_out = ord(s2[l]) - ord('a')

            # incoming char
            if need[idx_in] == window[idx_in]:
                matches -= 1
            window[idx_in] += 1
            if need[idx_in] == window[idx_in]:
                matches += 1

            # outgoing char
            if need[idx_out] == window[idx_out]:
                matches -= 1
            window[idx_out] -= 1
            if need[idx_out] == window[idx_out]:
                matches += 1

            l += 1

            if matches == 26:
                return True

        return False
