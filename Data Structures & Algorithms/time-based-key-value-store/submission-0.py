class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.time_map[key]) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if self.time_map[key][mid][0] == timestamp:
                return self.time_map[key][mid][1]
            elif self.time_map[key][mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        return self.time_map[key][r][1] if r >= 0 else ""
