# https://leetcode.com/problems/time-based-key-value-store/
class TimeMap:
    def __init__(self):
        self.timeMap = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap.keys():
            self.timeMap[key].append([timestamp, value])
        else:
            self.timeMap[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key in self.timeMap.keys():
            tempList = self.timeMap[key]

            if tempList[-1][0] <= timestamp:
                return tempList[-1][1]

            l = 0
            r = len(tempList) - 1
            diff = float('inf')


            while l <= r:
                mid = l + (r - l) // 2

                if tempList[mid][0] == timestamp:
                    return tempList[mid][1]

                elif tempList[mid][0] < timestamp:
                    tempDiff = timestamp - tempList[mid][0]

                    if tempDiff < diff:
                        diff = tempDiff
                        res = tempList[mid][1]

                    l = mid + 1

                else:
                    r = mid - 1

        return res

        # print(self.timeMap)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))
print(timeMap.get("foo", 3))
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))