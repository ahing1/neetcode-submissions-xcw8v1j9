class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n = len(temperatures)

        for i in range(n):
            j = i + 1
            count = 0
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1

            if j == n:
                res.append(0)
            else:
                res.append(j - i)
    
        return res
