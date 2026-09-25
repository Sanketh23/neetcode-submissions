class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        valTimeList = self.timeMap[key]

        l, r = 0, len(valTimeList) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if valTimeList[mid][1] == timestamp:
                return valTimeList[mid][0]
            elif valTimeList[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                res = valTimeList[mid][0]
        
        return res
