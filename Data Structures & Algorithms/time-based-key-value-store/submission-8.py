class TimeMap:

    def __init__(self):
        self._time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._time_map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self._time_map:
            return ""
        
        time_list = self._time_map[key]

        left = 0
        right = len(time_list) - 1

        while left <= right:
            mid = (left + right) // 2

            if time_list[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        return time_list[right][1] if right >= 0 else ""
