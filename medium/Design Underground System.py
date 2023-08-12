class UndergroundSystem:

    def __init__(self):
        self.customerMap = {}   # id --> [start, start time]
        self.timeMap = {}   # (start, end) --> [total time, count] * Use tuple() for key as a list() is unhashable

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customerMap[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startEnd = (self.customerMap[id][0], stationName)
        timeTaken = t - self.customerMap[id][1]

        if startEnd in self.timeMap:
            self.timeMap[startEnd][0] += timeTaken
            self.timeMap[startEnd][1] += 1
        else:
            self.timeMap[startEnd] = [timeTaken, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.timeMap[(startStation, endStation)][0] / self.timeMap[(startStation, endStation)][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)